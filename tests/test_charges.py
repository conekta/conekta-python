#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>
#(c) 2014- Leo Fischer / Conekta <@leofischer/@conektaio>

from . import BaseEndpointTestCase

class OrdersEndpointTestCase(BaseEndpointTestCase):

    def test_01_card_charge_complete(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        charge = self.client.Charge.create(self.card_charge_object)
        assert charge.id
        assert charge.status == 'paid'
        charge.find(charge.id)
        assert charge.id
        assert charge.status == 'paid'
        charge.refund(10000)
        self.assertEqual(charge['status'], 'partially_refunded')
        charge.refund()
        self.assertEqual(charge['status'], 'refunded')
        retrieved_charge = self.client.Charge.find(charge.id)
        assert charge.id

    def test_02_cash_charge_done(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        charge = self.client.Charge.create(self.cash_charge_object)
        assert charge.id

    def test_03_bank_charge_done(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        charge = self.client.Charge.create(self.bank_charge_object)
        assert charge.id

    def test_04_card_charge_authentication_fail(self):
        self.client.api_key = ''
        self.assertRaises(self.client.ConektaError, self.client.Charge.create, self.card_charge_object)

    def test_05_cash_charge_authentication_fail(self):
        self.client.api_key = ''
        self.assertRaises(self.client.ConektaError, self.client.Charge.create, self.cash_charge_object)

    def test_06_bank_charge_authentication_fail(self):
        self.client.api_key = ''
        self.assertRaises(self.client.ConektaError, self.client.Charge.create, self.bank_charge_object)

    def test_07_plan_create(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        plan = self.client.Plan.create(self.plan_object)
        assert plan.id == self.plan_object['id']
        plan = self.client.Plan.find(plan.id)
        assert plan.id == self.plan_object['id']

    def test_08_customer_create(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        customer = self.client.Customer.create(self.customer_object)
        assert customer.name == self.customer_object['name']

    def test_09_cards(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        customer = self.client.Customer.where({})[0]
        card = customer.createCard({'token_id':'tok_test_visa_4242'})
        assert card.last4 == '4242'
        card.update({'token_id':'tok_test_mastercard_5100'})
        assert card.last4 == '5100'
        card.update({'active':False})
        assert card.active == False
        card.delete()
        assert card.deleted

    def test_10_subscription(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        customer = self.client.Customer.where({})[0]
        subscription = customer.subscription
        if customer.subscription is None:
            subscription = customer.createSubscription({'plan_id':self.plan_object['id']})
        assert subscription.id
        subscription.pause()
        assert subscription.status == 'paused'
        subscription.resume()
        assert subscription.status == 'active'
        subscription.cancel()
        assert subscription.status == 'canceled'

    def test_11_customer_delete(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        customer = self.client.Customer.where({})[0]
        customer.delete()
        assert customer.deleted

    def test_12_plan_delete(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        plan = self.client.Plan.find(self.plan_object['id'])
        plan.delete()
        assert plan.deleted

    def test_13_cash_charge_done(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        charge_hash = self.card_charge_object.copy()
        charge_hash['capture'] = False

        charge = self.client.Charge.create(charge_hash)
        assert charge.id

        charge.capture
        assert charge.status == 'pre_authorized'

    def test_14_spei_charge_done(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        charge = self.client.Charge.create(self.spei_charge_object)
        assert charge.id

    def test_15_spei_charge_authentication_fail(self):
        self.client.api_key = ''
        self.assertRaises(self.client.ConektaError, self.client.Charge.create, self.spei_charge_object)
