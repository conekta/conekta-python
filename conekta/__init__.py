#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>

import os
import base64
import inspect
import requests
import urllib
import time
import platform

try:
    import json
except ImportError:
    import simplejson as json

API_VERSION = '2.0.0'

__version__ = '2.6.0'
__author__ = 'Leo Fischer'

API_BASE = 'https://api.conekta.io/'

data = {
    'lang' : 'python',
    'lang_version' : platform.python_version(),
    'publisher' : 'conekta',
    'bindings_version' : __version__,
    'uname' : platform.uname()
}

HEADERS = {
    'Accept': 'application/vnd.conekta-v%s+json' % (API_VERSION),
    'Content-type': 'application/json',
    'X-Conekta-Client-User-Agent' : json.dumps(data)
}

api_key = ''
locale = 'en'

class ConektaError(Exception):
  def __init__(self, error_json):
      super(ConektaError, self).__init__(error_json)
      self.error_json = error_json
      try:
        self.details = self.error_json['details']
        self.message = self.details[0]['message']
        self.debug_message = self.details[0]['debug_message']
        self.code = self.details[0]['code']
      except Exception:
        self.details = [
            {
                "message": "Hubo un error de comunicación Por favor intenta más tarde.",
                "debug_message": "Error message was unparsable",
                "code": "conekta.error.unparsable_error"
            }
        ]
        self.message = "Hubo un error de comunicación Por favor intenta más tarde."
        self.debug_message = "Error message was unparsable"
        self.code = "conekta.error.unparsable_error"

  def __str__(self):
      str(self.message)

class MalformedRequestError(ConektaError): pass
class AuthenticationError(ConektaError): pass
class ProcessingError(ConektaError): pass
class ResourceNotFoundError(ConektaError): pass
class ParameterValidationError(ConektaError): pass
class ApiError(ConektaError): pass

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
        CA_PATH = os.path.join(os.path.dirname(__file__), 'ssl_data/ca_bundle.crt')
        if method == 'GET':
            if params is None:
                url = absolute_url
            else:
                try:
                    url = "%s?%s" % (absolute_url, urllib.parse.urlencode(params, True))
                except AttributeError:
                    url = "%s?%s" % (absolute_url, urllib.urlencode(params, True))
            body = requests.request(method, url, headers=HEADERS, verify=CA_PATH)
        else:
            if params is None:
                params = ''
            body = requests.request(method, absolute_url, headers=HEADERS, verify=CA_PATH, data=json.dumps(params))
            
        headers = body.headers
        headers['status'] = str(body.status_code)
        body = body._content
        try:
            body = str(body, 'utf-8')
        except TypeError:
            body = str(body)

        if headers['status'] == '200' or headers['status'] == '201':
            response_body = json.loads(body)
            return response_body

        if headers['status'] == '400' or headers['status'] == '400':
            raise MalformedRequestError(json.loads(body))
        elif headers['status'] == '401' or headers['status'] == '401':
            raise AuthenticationError(json.loads(body))
        elif headers['status'] == '402' or headers['status'] == '402':
            raise ProcessingError(json.loads(body))
        elif headers['status'] == '404' or headers['status'] == '404':
            raise ResourceNotFoundError(json.loads(body))
        elif headers['status'] == '422' or headers['status'] == '422':
            raise ParameterValidationError(json.loads(body))
        elif headers['status'] == '500' or headers['status'] == '500':
            raise ApiError(json.loads(body))
        else:
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

class _EventableResource(_Resource):

    def events(self, params={}, api_key=None):
        uri = self.instance_url()
        if hasattr(self, 'parent'):
            uri = "%s/%s" % (self.instance_url(), self.id)

        event = Event.load_url("%s/events" % uri, 'GET', params, api_key=api_key)
        return Event(event)

class _DeletableResource(_Resource):

    def delete(self, params={}, list_to_remove=None, uri=None, api_key=None):
        if uri is None:
            uri = self.instance_url()

            if hasattr(self, 'parent'):
                uri = "%s/%s" % (self.instance_url(), self.id)



        object_reponse = self.load_via_http_request(uri, 'DELETE', {}, api_key=api_key)

        if list_to_remove != None:
            for remove_object in list_to_remove:
                if remove_object.id == self.id:
                    list_to_remove.remove(remove_object)
                    break

        return object_reponse

class _UpdatableResource(_Resource):

    def update(self, params={}, api_key=None):
        uri = self.instance_url()

        if hasattr(self, 'parent') and not isinstance(self, Subscription):
            uri = "%s/%s" % (self.instance_url(), self.id)

        return self.load_via_http_request(uri, 'PUT', params, api_key=api_key)

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

        response = cls.load_url(endpoint, 'GET', query, api_key=api_key)
        pag = Pagination(response)
        data = response["data"]

        pag.data = []
        for obj in data:
            new_obj = None
            if obj["object"] == "customer":
                new_obj = Customer(obj)
                pag.class_name = Customer

            elif obj["object"] == "order":
                new_obj = Order(obj)
                pag.class_name = Order

            elif obj["object"] == "log":
                new_obj = Log(obj)
                pag.class_name = Log

            pag.data.append(new_obj)


        return pag

    #DEPRECATED aliased method, will be removed in next major release
    @classmethod
    def get(cls, _id, api_key=None):
        cls.find(_id, api_key)

class Card(_UpdatableResource, _DeletableResource):

    def instance_url(self):
        return "customers/%s/cards/%s" % (self.parent.id, self.id)

class Charge(_CreatableResource, _FindableResource):

    def instance_url(self):
        return "orders/%s/charges" % (self.parent.id)

    def refund(self, amount=None, api_key=None):
        if amount is None:
            return self.load_via_http_request("%s/refund" % self.instance_url(), api_key=api_key)
        else:
            return self.load_via_http_request("%s/refund" % self.instance_url(), 'POST', {'amount':amount}, api_key=api_key)

    def capture(self, api_key=None):
        return self.load_via_http_request("%s/capture" % self.instance_url(), api_key=api_key)

class Order(_CreatableResource, _UpdatableResource, _DeletableResource, _FindableResource, _EventableResource):
    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        attributes = args[0]
        self.currency = attributes['currency']
        self.line_items = []
        self.tax_lines = []
        self.shipping_lines = []
        self.discount_lines = []
        self.charges = []
        query = {}
        if 'line_items' in attributes.keys():
            endpoint = 'orders/{}/line_items'.format(attributes['id'])
            response = self.load_url(endpoint,'GET',query,api_key=api_key)
            for line_item in response["data"]:
                new_line_item = LineItem(line_item)
                new_line_item.parent = self
                self.line_items.append(new_line_item)

        if 'tax_lines' in attributes.keys():
            for tax_line in attributes['tax_lines']["data"]:
                new_tax_line = TaxLine(tax_line)
                new_tax_line.parent = self
                self.tax_lines.append(new_tax_line)

        if 'shipping_lines' in attributes.keys():
            for shipping_line in attributes['shipping_lines']["data"]:
                new_shipping_line = ShippingLine(shipping_line)
                new_shipping_line.parent = self
                self.shipping_lines.append(new_shipping_line)

        if 'discount_lines' in attributes.keys():
            for discount_line in attributes['discount_lines']["data"]:
                new_discount_line = DiscountLine(discount_line)
                new_discount_line.parent = self
                self.discount_lines.append(new_discount_line)

        if 'customer_info' in attributes.keys():
            self.customer_info = CustomerInfo(attributes['customer_info'])

        if 'shipping_contact' in attributes.keys():
            self.shipping_contact = ShippingContact(attributes['shipping_contact'])

        if 'charges' in attributes.keys():
            for charge in attributes['charges']["data"]:
                payment_method = None
                if charge['payment_method'] is not None:
                    payment_method = PaymentMethod(charge['payment_method'])
                charge = Charge(charge)
                charge.payment_method = payment_method
                self.charges.append(charge)

        if 'checkout' in attributes.keys():
            self.checkout = CheckoutOrder(attributes['checkout'])

    def capture(self, params={}, api_key=None):
        order = Order.load_url("%s/capture" % (self.instance_url()), 'PUT', params, api_key=api_key)
        time.sleep(2)
        new_order = Order.find(self.id)
        self.charges = new_order.charges
        self.payment_status = new_order.payment_status
        return new_order

    def refund(self, params={}, api_key=None):
        order_refund = Order.load_url("%s/refund" % (self.instance_url()), 'POST', params, api_key=api_key)
        time.sleep(2)
        new_order = Order.find(self.id)
        self.charges = new_order.charges
        self.payment_status = new_order.payment_status
        return new_order

    def void(self, params={}, api_key=None):
        order_refund = Order.load_url("%s/void" % (self.instance_url()), 'POST', params, api_key=api_key)
        time.sleep(2)
        new_order = Order.find(self.id)
        self.charges = new_order.charges
        self.payment_status = new_order.payment_status
        return new_order

    def charge(self, params, api_key=None):
        charge = Charge(Charge.load_url("%s/charges" % self.instance_url(), 'POST', params, api_key=api_key))
        self.charges.append(charge)
        return charge

    def createShippingContact(self, params, api_key=None):
        orders = self.update(params)
        self.shipping_contact = ShippingContact(orders['shipping_contact'])
        return self.shipping_contact

    def createLineItem(self, params, api_key=None):
        line_item = LineItem(LineItem.load_url("%s/line_items" % self.instance_url(), 'POST', params, api_key=api_key))
        self.line_items.append(line_item)
        return line_item

    def createTaxLine(self, params, api_key=None):
        tax_line = TaxLine(TaxLine.load_url("%s/tax_lines" % self.instance_url(), 'POST', params, api_key=api_key))
        self.tax_lines.append(tax_line)
        return tax_line

    def createShippingLine(self, params, api_key=None):
        shipping_line = ShippingLine(ShippingLine.load_url("%s/shipping_lines" % self.instance_url(), 'POST', params, api_key=api_key))
        self.shipping_lines.append(shipping_line)
        return shipping_line

    def createDiscountLine(self, params, api_key=None):
        discount_line = DiscountLine(DiscountLine.load_url("%s/discount_lines" % self.instance_url(), 'POST', params, api_key=api_key))
        self.discount_lines.append(discount_line)
        return discount_line

    def createCheckout(self, params, api_key=None):
        checkout = CheckoutOrder(DiscountLine.load_url("%s/orders" % self.instance_url(), 'POST', params, api_key=api_key))
        self.checkout.append(checkout)
        return checkout

class CustomerInfo(_UpdatableResource): pass

class OrderReturns(_UpdatableResource): pass

class PaymentMethod(_UpdatableResource): pass

class Address(_FindableResource): pass

class Customer(_CreatableResource, _UpdatableResource, _DeletableResource, _FindableResource, _EventableResource):

    def __init__(self, *args, **kwargs):
        super(Customer, self).__init__(*args, **kwargs)

        attributes = args[0]
        self.payment_sources   = []
        self.shipping_contacts = []
        if 'payment_sources' in attributes.keys():
            for payment_source in attributes['payment_sources']['data']:
                new_payment_source = PaymentSource(payment_source)
                new_payment_source.parent = self
                self.payment_sources.append(new_payment_source)

        if 'shipping_contacts' in attributes.keys():
            for shipping_contact in attributes['shipping_contacts']['data']:
                new_shipping_contact = ShippingContact(shipping_contact)
                new_shipping_contact.address = Address(shipping_contact["address"])
                new_shipping_contact.parent = self
                self.shipping_contacts.append(new_shipping_contact)

        if 'subscription' in attributes.keys() and isinstance(attributes['subscription'], dict):
            attributes['subscription']['parent'] = self
            self.subscription = Subscription(attributes['subscription'])
        else:
            self.subscription = None

    def createPaymentSource(self, params, api_key=None):
        pay_src = PaymentSource.load_url("%s/payment_sources" % self.instance_url(), 'POST', params, api_key=api_key)
        payment_source = PaymentSource(pay_src)
        payment_source.parent = self
        self.payment_sources.append(payment_source)
        return payment_source

    def createShippingContact(self, params, api_key=None):
        shipping = PaymentSource.load_url("%s/shipping_contacts" % self.instance_url(), 'POST', params, api_key=api_key)
        shipping_contact = ShippingContact(shipping)
        shipping_contact.parent = self
        self.shipping_contacts.append(shipping_contact)
        return shipping_contact

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

class Checkout(_CreatableResource, _UpdatableResource, _DeletableResource, _FindableResource):

    def __init__(self, *args, **kwargs):
        super(Checkouts, self).__init__(*args, **kwargs)
        
    def create(self, params, api_key=None):
        return self.load_via_http_request("%s/checkouts" % self.instance_url(), 'POST', params, api_key=api_key)

    def cancel(self, params, api_key=None):
        return self.load_via_http_request("%s/checkouts/cancel/%s" % (self.instance_url(), self.id), 'PUT', None, api_key=api_key)

    def sendEmail(self, params, api_key=None):
        return self.load_via_http_request("%s/checkouts/email" % self.instance_url(), 'POST', params, api_key=api_key)

    def sendSms(self, params, api_key=None):
        return self.load_via_http_request("%s/checkouts/sms" % self.instance_url(), 'POST', params, api_key=api_key)

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
class Pagination(_CreatableResource):
    def next(self):
        if not hasattr(self, 'next_page_url'):
            return None

        raw_params = self.next_page_url.split("?")[1]
        query = {}
        for elemet_params in raw_params.split("&"):
            key_and_param = elemet_params.split("=")
            query[key_and_param[0]] = key_and_param[1]
        return self.class_name.where(query)

    def before(self):
        if not hasattr(self, 'previous_page_url'):
            return None
        raw_params = self.previous_page_url.split("?")[1]
        query = {}
        for elemet_params in raw_params.split("&"):
            key_and_param = elemet_params.split("=")
            query[key_and_param[0]] = key_and_param[1]
        return self.class_name.where(query)

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

class LineItem(_CreatableResource, _UpdatableResource, _DeletableResource, _FindableResource, _EventableResource):

    def instance_url(self):
        return "orders/%s/line_items" % (self.parent.id)

    def delete(self, params={}, api_key=None):
        return super(LineItem, self).delete(params, self.parent.line_items)

class TaxLine(_CreatableResource, _UpdatableResource, _DeletableResource, _FindableResource, _EventableResource):

    def instance_url(self):
        return "orders/%s/tax_lines" % (self.parent.id)

    def delete(self, params={}, api_key=None):
        return super(TaxLine, self).delete(params, self.parent.tax_lines)

class ShippingLine(_CreatableResource, _UpdatableResource, _DeletableResource, _FindableResource, _EventableResource):

    def instance_url(self):
        return "orders/%s/shipping_lines" % (self.parent.id)

    def delete(self, params={}, api_key=None):
        return super(ShippingLine, self).delete(params, self.parent.shipping_lines)

class DiscountLine(_CreatableResource, _UpdatableResource, _DeletableResource, _FindableResource, _EventableResource):

    def instance_url(self):
        return "orders/%s/discount_lines" % (self.parent.id)

    def delete(self, params={}, api_key=None):
        return super(DiscountLine, self).delete(params, self.parent.discount_lines)

class PaymentSource(_CreatableResource, _UpdatableResource, _DeletableResource, _FindableResource):
    def instance_url(self):
        return "customers/%s/payment_sources" % (self.parent.id)

    def delete(self, params={}, api_key=None):
        return super(PaymentSource, self).delete(params, self.parent.payment_sources)

    def events(self, params={}, api_key=None):
        uri = "%s/payment_sources/%s/events" % (self.parent.instance_url(), self.id)
        event = Event.load_url(uri, 'GET', params, api_key=api_key)
        return Event(event)

class ShippingContact(_CreatableResource, _UpdatableResource, _DeletableResource, _FindableResource):

    def instance_url(self):
        return "customers/%s/shipping_contacts" % (self.parent.id)

    def update(self, params={}, api_key=None):
        uri = "%s/shipping_contacts/%s" % (self.parent.instance_url(), self.id)
        return self.load_via_http_request(uri, 'PUT', params, api_key=api_key)

    def delete(self, params={}, api_key=None):
        uri = "%s/shipping_contacts/%s" % (self.parent.instance_url(), self.id)
        return super(ShippingContact, self).delete(params, self.parent.shipping_contacts, uri)

    def events(self, params={}, api_key=None):
        uri = "%s/shipping_contacts/%s/events" % (self.parent.instance_url(), self.id)
        return Event(Event.load_url(uri, 'GET', params, api_key=api_key))

class CheckoutOrder(_CreatableResource, _UpdatableResource, _DeletableResource, _FindableResource):

        def instance_url(self):
        return "orders" 