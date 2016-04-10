#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>

import os
import base64
import inspect
import urllib
from httplib2 import Http

try:
    import json
except ImportError:
    import simplejson as json

API_VERSION = '1.0.0'

__version__ = '1.1.0'
__author__ = 'Leo Fischer'

API_BASE = 'https://api.conekta.io/'

HEADERS = {
    'Accept': 'application/vnd.conekta-v%s+json' % (API_VERSION),
    'Content-type': 'application/json'
}

api_key = ''
locale = 'en'

class ConektaError(Exception):
  def __init__(self, error_json):
      super(ConektaError, self).__init__(error_json)
      self.error_json = error_json

class _Resource(object):
    def __init__(self, attributes):
        self.initialize_instance(attributes)

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    @classmethod
    def build_http_request(cls, method, path, params, _api_key=None):
        if _api_key is None:
            HEADERS['Authorization'] = 'Basic %s' % (base64.b64encode((api_key + ':').encode('utf-8'))).decode('ascii')
        else:
            HEADERS['Authorization'] = 'Basic %s' % (base64.b64encode((_api_key + ':').encode("utf-8"))).decode('ascii')

        if not locale is None:
            HEADERS['Accept-Language'] = locale

        absolute_url = API_BASE + path
        request = Http(ca_certs=os.path.join(os.path.dirname(__file__), 'ssl_data/ca_bundle.crt')).request
        if method == 'GET':
            if params is None:
                url = absolute_url
            else:
                try:
                    url = "%s?%s" % (absolute_url, urllib.parse.urlencode(params, True))
                except AttributeError:
                    url = "%s?%s" % (absolute_url, urllib.urlencode(params, True))
                  
            headers, body = request(url, method, headers=HEADERS)
        else:
            if params is None:
                HEADERS['Content-type'] = 'application/x-www-form-urlencoded'
                HEADERS['Content-length'] = '0'
                headers, body = request(absolute_url, method, headers=HEADERS, body='')
                del HEADERS['Content-length']
                HEADERS['Content-type'] = 'application/json'
            else:
                headers, body = request(absolute_url, method, headers=HEADERS, body=json.dumps(params))

        try:
            body = str(body, 'utf-8')
        except TypeError:
            body = str(body)

        if headers['status'] == '200' or headers['status'] == '201':
            response_body = json.loads(body)
            return response_body
        raise ConektaError(json.loads(body))

    @classmethod
    def load_url(cls, path, method='GET', params=None, api_key=None):
        response = cls.build_http_request(method, path, params, _api_key = api_key)
        return response

    @classmethod
    def class_name(cls):
        try:
            return "%s" % urllib.parse.quote_plus(cls.__name__.lower())
        except AttributeError:
            return "%s" % urllib.quote_plus(cls.__name__.lower())

    @classmethod
    def class_url(cls):
        return "%ss" % cls.class_name()

    def instance_url(self):
        return "%s/%s" % (self.class_url(), self.id)

    def initialize_instance(self, attributes):
        if 'id' in attributes.keys():
            self.id = attributes['id']

        existing_keys = self.__dict__.keys()
        new_keys = attributes.keys()

        old_keys = (set(existing_keys) - set(['parent'])) - set(new_keys)
        for key in old_keys:
            self.__dict__[key] = None

        for key in new_keys:
            self.__dict__[key] = attributes[key]


    def load_via_http_request(self, url=None, method='POST', params=None, api_key=None):
        if url is None:
            url = self.instance_url()
            method = 'GET'

        response = self.load_url(url, method=method, params=params, api_key=api_key)

        self.initialize_instance(response)

        return self

class _DeletableResource(_Resource):

    def delete(self, params={}, api_key=None):
        return self.load_via_http_request(self.instance_url(), 'DELETE', {}, api_key=api_key)

class _UpdatableResource(_Resource):

    def update(self, params={}, api_key=None):
        return self.load_via_http_request(self.instance_url(), 'PUT', params, api_key=api_key)

class _CreatableResource(_Resource):

    @classmethod
    def create(cls, params, api_key=None):
        endpoint = cls.class_url()
        return cls(cls.load_url(endpoint, method='POST', params=params, api_key=api_key))

class _FindableResource(_Resource):

    @classmethod
    def find(cls, _id, api_key=None):
        endpoint = cls.class_url()
        return cls(cls.load_url("%s/%s" % (endpoint, _id), api_key=api_key ))

    @classmethod
    def where(cls, query={}, limit=10, offset=0, sort=[], api_key=None):
        endpoint = cls.class_url()
        query['limit'] = limit
        query['offset'] = offset
        query['sort'] = sort
        return [cls(attributes) for attributes in cls.load_url(endpoint, 'GET', query, api_key=api_key)]

    #DEPRECATED aliased method, will be removed in next major release
    @classmethod
    def get(cls, _id, api_key=None):
        cls.find(_id, api_key)

class Card(_UpdatableResource, _DeletableResource): 

    def instance_url(self):
        return "customers/%s/cards/%s" % (self.parent.id, self.id)

class Charge(_CreatableResource, _FindableResource):

    def refund(self, amount=None, api_key=None):
        if amount is None:
            return self.load_via_http_request("%s/refund" % self.instance_url(), api_key=api_key)
        else:
            return self.load_via_http_request("%s/refund" % self.instance_url(), 'POST', {'amount':amount}, api_key=api_key)

    def capture(self, api_key=None):
        return self.load_via_http_request("%s/capture" % self.instance_url(), api_key=api_key)

class Customer(_CreatableResource, _UpdatableResource, _DeletableResource, _FindableResource):
    
    def __init__(self, *args, **kwargs):
        super(Customer, self).__init__(*args, **kwargs)

        attributes = args[0]
        self.cards = []
        if 'cards' in attributes.keys():
            for card in attributes['cards']:
                card['parent'] = self
                self.cards.append(Card(card))

        if 'subscription' in attributes.keys() and isinstance(attributes['subscription'], dict):
            attributes['subscription']['parent'] = self
            self.subscription = Subscription(attributes['subscription'])
        else:
            self.subscription = None

    def createCard(self, params, api_key=None):
        card = Card(Card.load_url("%s/cards" % self.instance_url(), 'POST', params, api_key=api_key))
        card.parent = self
        self.cards.append(card)
        return card

    def createSubscription(self, params, api_key=None):
        subscription = Subscription(Subscription.load_url("%s/subscription" % self.instance_url(), 'POST', params, api_key=api_key))
        subscription.parent = self
        self.subscription = subscription
        return subscription

    @property
    def default_card(self):
        if self.default_card_id:
            return [card for card in self.cards if card.id == self.default_card_id][0]
        else:
            return None

class Event(_FindableResource): pass

class Log(_FindableResource): pass

class Payee(_CreatableResource, _UpdatableResource, _DeletableResource, _FindableResource):

    def __init__(self, *args, **kwargs):
        super(Payee, self).__init__(*args, **kwargs)

        attributes = args[0]
        self.payout_methods = []
        if 'payout_methods' in attributes.keys():
            for payout_method in attributes['payout_methods']:
                payout_method['parent'] = self
                self.payout_methods.append(PayoutMethod(payout_method))

    def createPayoutMethod(self, params, api_key=None):
        payout_method = PayoutMethod(PayoutMethod.load_url("%s/payout_methods" % self.instance_url(), 'POST', params, api_key=api_key))
        payout_method.parent = self
        self.payout_methods.append(payout_method)
        return payout_method

    @property
    def default_payout_method(self):
        if self.default_payout_method_id:
            return [payout_method for payout_method in self.payout_methods if payout_method.id == self.default_payout_method_id][0]
        else:
            return None

class Payout(_CreatableResource, _FindableResource): pass

class PayoutMethod(_UpdatableResource, _DeletableResource): 

    def instance_url(self):
        return "payees/%s/payout_methods/%s" % (self.parent.id, self.id)

class Plan(_CreatableResource, _UpdatableResource, _DeletableResource, _FindableResource): pass

class Subscription(_UpdatableResource):

    def instance_url(self):
        return "customers/%s/subscription" % (self.parent.id)

    def pause(self, finish_billing_cycle=False, until=None, api_key=None):
        return self.load_via_http_request("%s/pause" % self.instance_url(), 'POST', {'until': until}, api_key=api_key)

    def resume(self, api_key=None):
        return self.load_via_http_request("%s/resume" % self.instance_url(), 'POST', None, api_key=api_key)

    def cancel(self, finish_billing_cycle=False, api_key=None):
        return self.load_via_http_request("%s/cancel" % self.instance_url(), 'POST', None, api_key=api_key)

    @property
    def card(self):
        return [card for card in self.parent.cards if card.id == self.card_id][0]

    @property
    def plan(self):
        return Plan.retrieve(self.plan_id)

class Webhook(_CreatableResource, _UpdatableResource, _DeletableResource, _FindableResource): pass

