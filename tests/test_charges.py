#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb> 

from . import BaseEndpointTestCase


class OrdersEndpointTestCase(BaseEndpointTestCase):

    def test_card_charge_done(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        response = self.client.Charge.create(self.card_charge_object)
        assert 'id' in response.parseJSON()

    def test_cash_charge_done(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        response = self.client.Charge.create(self.cash_charge_object)
        assert 'id' in response.parseJSON()

    def test_bank_charge_done(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        response = self.client.Charge.create(self.bank_charge_object)
        assert 'id' in response.parseJSON()

    def test_card_charge_authentication_fail(self):
        self.client.api_key = ''
        response = self.client.Charge.create(self.card_charge_object)
        assert 'authentication_error' == response.parseJSON()['error']['type']

    def test_cash_charge_authentication_fail(self):
        self.client.api_key = ''
        response = self.client.Charge.create(self.cash_charge_object)
        assert 'authentication_error' == response.parseJSON()['error']['type']

    def test_bank_charge_authentication_fail(self):
        self.client.api_key = ''
        response = self.client.Charge.create(self.bank_charge_object)
        assert 'authentication_error' == response.parseJSON()['error']['type']


class OrdersEndpointTestCaseWithCustomAPIKey(BaseEndpointTestCase):
    """ The same tests as in OrdersEndpointTestCase but not
    setting the API key globally rather than using it differently
    for each call """

    def test_card_charge_done(self):
        self.client.api_key = ''
        response = self.client.Charge.create(self.card_charge_object, other_api_key='1tv5yJp3xnVZ7eK67m4h')
        assert 'id' in response.parseJSON()

    def test_cash_charge_done(self):
        self.client.api_key = ''
        response = self.client.Charge.create(self.cash_charge_object, other_api_key='1tv5yJp3xnVZ7eK67m4h')
        assert 'id' in response.parseJSON()

    def test_bank_charge_done(self):
        self.client.api_key = ''
        response = self.client.Charge.create(self.bank_charge_object, other_api_key='1tv5yJp3xnVZ7eK67m4h')
        assert 'id' in response.parseJSON()

    def test_card_charge_authentication_fail(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        response = self.client.Charge.create(self.card_charge_object, other_api_key='')
        assert 'authentication_error' == response.parseJSON()['error']['type']

    def test_cash_charge_authentication_fail(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        response = self.client.Charge.create(self.cash_charge_object, other_api_key='')
        assert 'authentication_error' == response.parseJSON()['error']['type']

    def test_bank_charge_authentication_fail(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        response = self.client.Charge.create(self.bank_charge_object, other_api_key='')
        assert 'authentication_error' == response.parseJSON()['error']['type']


