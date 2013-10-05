#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>

import inspect
from httplib2 import Http

try:
    import json
except ImportError:
    import simplejson as json

API_VERSION = '0.6'

__version__ = API_VERSION
__author__ = 'Julian Ceballos'

API_BASE = 'https://api.conekta.io/'

HEADERS = {
    'Accept': 'application/vnd.example.v1',
    'Content-type': 'application/json'
}

api_key = ''

def parseJSON(obj):
    data = {}
    items = ()
    if isinstance(obj, _CkObject):
        items = obj.__dict__.iteritems()
    else:
        try:
            items = json.loads(obj).iteritems()
        except:
            items = obj.iteritems()
    for key, value in items:
        try:
            data[key] = parseJSON(value)
        except AttributeError:
            data[key] = value
    return data

class _CkObject(object):
    def __init__(self, d):
        self.__dict__['d'] = d

    def __getattr__(self, key):
        value = self.__dict__['d'][key]
        if type(value) == type({}):
            return _CkObject(value)
        return value

    def parseJSON(self):
        data = parseJSON(self)
        return data['d']

class _Endpoint(object):

    def expand_path(self, path):
        return API_BASE + path

    def build_request(self, method, path, params, other_api_key=None):
        HEADERS['Authorization'] = 'Token token="%s"' % (api_key if other_api_key is None else other_api_key)
        absolute_url = self.expand_path(path)
        request = Http({}).request
        headers, body = request(absolute_url, method, headers=HEADERS, body=json.dumps(params))
        if headers['status'] == '200' or headers['status'] == '201':
            return _CkObject(json.loads(body))
        return _CkObject({'error': json.loads(body)})

    def load_url(self, path, method='get', params={}, other_api_key=None):
        response = self.build_request(method, path, params, other_api_key)
        return response

class _Charges(_Endpoint):

    def create(self, params, other_api_key=None):
        endpoint = 'charges.json'
        return self.load_url(endpoint, method='post', params=params, other_api_key=other_api_key)

class _Event(_Endpoint):

    def all(self, other_api_key=None):
        endpoint = 'events.json'
        return self.load_url(endpoint, other_api_key=other_api_key)


Charge = _Charges()
Event = _Event()
