#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>
#(c) 2014- Leo Fischer / Conekta <@leofischer/@conektaio>

from . import BaseEndpointTestCase

class OrdersEndpointTestCase(BaseEndpointTestCase):

    def test_01_payee_create(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        payee = self.client.Payee.create(self.payee_object)
        assert payee.name == self.payee_object['name']
        assert payee.payout_methods[0]
        assert payee.payout_methods[0].account_number == self.payee_object['bank']['account_number']

    def test_02_payout_methods(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        payee = self.client.Payee.where({})[0]
        payout_method = payee.createPayoutMethod(self.payout_method_object)
        assert payout_method.account_number == self.payout_method_object['account_number']
        payout_method.update({'account_number':'098765432101234564'})
        assert payout_method.account_number == '098765432101234564'
        payout_method.update({'active':False})
        assert payout_method.active == False
        payout_method.delete()
        assert payout_method.deleted

    def test_03_payout_cash_charge_done(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        payee = self.client.Payee.where({})[0]
        assert payee.id
        payout = self.client.Payout.create({
            'payee': payee.id,
            'amount': 1000,
            'currency': 'MXN'
        })

        assert payout.id
        assert payout.amount == 1000
