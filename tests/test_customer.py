#!/usr/bin/python
#coding: utf-8
#(c) 2017 Ramses Carbajal <@RamsesCarbajal>
from . import BaseEndpointTestCase

class OrdersEndpointTestCase(BaseEndpointTestCase):

    def test_01_customer_create(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        customer = self.client.Customer.create(self.customer_object.copy())
        payment_source = customer.payment_sources[0]
        shipping_contact = customer.shipping_contacts[0]

        assert customer.name  == 'James Howlett'
        assert customer.email == 'logan@x-men.org'
        assert customer.phone == '+525511223344'
        assert payment_source.brand == 'VISA' or payment_source.brand == 'MC'
        assert payment_source.last4 == '4242' or payment_source.last4 == '5100'
        assert payment_source.type  == 'card'

        assert shipping_contact.receiver        == "Marvin Fuller"
        assert shipping_contact.between_streets == "Ackerman Crescent"
        assert shipping_contact.address.city    == "Red Deer"

    def test_02_customer_add_token(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        customer_params = self.customer_object.copy()
        del customer_params["payment_sources"]
        customer = self.client.Customer.create(customer_params)
        payment_source = customer.createPaymentSource(self.payment_source_object.copy())

        assert payment_source.brand == "VISA"
        assert payment_source.last4 == "4242"

    def test_03_customer_update_payment_source(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        customer = self.client.Customer.create(self.customer_object.copy())
        payment_source = customer.payment_sources[0]
        payment_source.update(self.update_payment_source_object.copy())
        payment_source = customer.payment_sources[0]
        assert payment_source.brand == 'VISA' or payment_source.brand == 'MC'
        assert payment_source.last4 == '4242' or payment_source.last4 == '5100'

    def test_04_customer_delete_payment_source(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        customer = self.client.Customer.create(self.customer_object.copy())
        payment_source = customer.payment_sources[0]

        payment_source_deleted = payment_source.delete()

        assert payment_source_deleted.deleted == True

        payment_source = customer.payment_sources[0]

        assert payment_source.brand == 'VISA' or payment_source.brand == 'MC'
        assert payment_source.last4 == '4242' or payment_source.last4 == '5100'

    def test_08_customer_add_shipping_contact(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        customer_params = self.customer_object.copy()
        del customer_params["shipping_contacts"]
        customer = self.client.Customer.create(customer_params)
        shipping_contact = customer.createShippingContact(self.shipping_contact_object.copy())

        assert shipping_contact.phone           == "+525511008811"
        assert shipping_contact.receiver        == "Dr. Manhatan"
        assert shipping_contact.between_streets == "some streets"

    def test_09_customer_update_plan(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        customer = self.client.Customer.create(self.customer_object.copy())
        customer.createSubscription({"plan":"gold-plan"})
        customer.subscription.update({"plan":"opal-plan"})
        customer2 = self.client.Customer.find(customer.id)

        assert customer2.subscription.plan_id == "opal-plan"
