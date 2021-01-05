#!/usr/bin/python
#coding: utf-8
#(c) 2020 Erick Colin <@erickcolin>

from . import BaseEndpointTestCase

class CheckoutsEndpointTestCase(BaseEndpointTestCase):

    def test_01_create_checkout(self):
        
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        checkout = self.client.Checkout.create(self.checkout_object.copy())

        assert checkout.type == "PaymentLink"
        assert checkout.object == "checkout"
        assert checkout.status != "Issued"
        assert checkout.url.startswith("https:\\pay.conekta")
        assert checkout.id.len() == 36
    
    def test_02_create_checkout_recurrent(self):

        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        checkout = self.client.Checkout.create(self.checkout_object_multiple.copy())

        assert checkout.recurrent == True
        assert checkout.type == "PaymentLink"
        assert checkout.object == "checkout"
        assert checkout.url.startswith("https:\\pay.conekta")
        assert checkout.id.len() == 36

    
    def test_03_create_checkout_msi(self):

        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        checkout = self.client.Checkout.create(self.checkout_object_msi.copy())

        assert checkout.monthly_installments_enabled == True
        assert checkout.type == "PaymentLink"
        assert checkout.object == "checkout"
        assert checkout.url.startswith("https:\\pay.conekta")
        assert checkout.id.len() == 36

    def test_04_checkout_sendmail(self):

        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        checkout = self.client.Checkout.sendEmail(self.checkout_object_send.copy())

        assert isinstance(checkout,self.checkout_object_send.copy())

    def test_05_checkout_sendsms(self):

        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        checkout = self.client.Checkout.sendSms(self.checkout_object_send.copy())

        assert isinstance(checkout,self.checkout_object_send.copy())

    def test_06_checkout_cancel():

        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        checkout = self.client.Checkout.cancel(self.checkout_object_send.copy())

        assert checkout.status == "Cancelled"

    def test_07_orders_checkout_create(self)

       self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        order = self.checkout_order_object.copy()
        order = self.client.Order.create(order)
        checkout = order.createCheckout(self.checkout_order_object.copy())
        
        assert checkout.type == "Integration"
        assert checkout.status != "Issued"
        assert checkout.url.startswith("https:\\pay.conekta")
        assert checkout.id.len() == 36


    def test_08_orders_checkout_create_redireccion(self)

       self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        order = self.checkout_order__redirect_object.copy()
        order = self.client.Order.create(order)
        checkout = order.createCheckout(self.checkout_order__redirect_object.copy())
        
        assert checkout.type == "HostedPayment"
        assert checkout.status != "Issued"
        assert checkout.url.startswith("https:\\pay.conekta")
        assert checkout.id.len() == 36

    def test_09_orders_checkout__msi_create(self)

       self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        order = self.checkout_order_object.copy()
        order = self.client.Order.create(order)
        checkout = order.createCheckout(self.checkout_order_object.copy())
        
        assert checkout.monthly_installments_enabled = True,
        assert checkout.type == "Integration"
        assert checkout.status != "Issued"
        assert checkout.url.startswith("https:\\pay.conekta")
        assert checkout.id.len() == 36