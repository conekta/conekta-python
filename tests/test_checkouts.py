#!/usr/bin/python
# coding: utf-8
# (c) 2020 Erick Colin <@erickcolin>

from . import BaseEndpointTestCase


class CheckoutsEndpointTestCase(BaseEndpointTestCase):

    def test_01_create_checkout(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        checkout = self.client.Checkout.create(self.checkout_object.copy())

        assert checkout.type == "PaymentLink"
        assert checkout.object == "checkout"
        assert checkout.status == "Issued"
        assert checkout.url.startswith("https://pay.conekta")
        assert len(checkout.id) == 36

    def test_02_create_checkout_recurrent(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        checkout = self.client.Checkout.create(self.checkout_object_multiple.copy())

        assert checkout.recurrent == True
        assert checkout.type == "PaymentLink"
        assert checkout.object == "checkout"
        assert checkout.url.startswith("https://pay.conekta")
        assert len(checkout.id) == 36

    def test_03_create_checkout_msi(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        checkout = self.client.Checkout.create(self.checkout_object_msi.copy())

        assert checkout.monthly_installments_enabled == True
        assert checkout.type == "PaymentLink"
        assert checkout.object == "checkout"
        assert checkout.url.startswith("https://pay.conekta")
        assert len(checkout.id) == 36

    def test_04_checkout_sendmail(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        checkout = self.client.Checkout.create(self.checkout_object.copy())
        response = checkout.sendEmail(self.checkout_object_send.copy())

        assert response.emails_sent == 1

    def test_05_checkout_sendsms(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        checkout = self.client.Checkout.create(self.checkout_object.copy())
        response = checkout.sendSms(self.checkout_object_send.copy())

        assert response.sms_sent == 1

    def test_06_checkout_cancel(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        checkout = self.client.Checkout.create(self.checkout_object.copy())
        canceled_checkout = checkout.cancel(self.checkout_object_send.copy())

        assert canceled_checkout.status == "Cancelled"

    def test_07_orders_checkout_create(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        order = self.client.Order.create(self.checkout_order_object.copy())

        checkout = order.checkout
        assert checkout.type == "Integration"
        assert checkout.status == "Issued"
        assert len(checkout.id) == 36

    def test_08_orders_checkout_create_redirection(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        order = self.client.Order.create(self.checkout_order__redirect_object.copy())

        checkout = order.checkout
        assert checkout.type == "HostedPayment"
        assert checkout.status == "Issued"
        assert checkout.url.startswith("https://pay.conekta")
        assert len(checkout.id) == 36

    def test_09_orders_checkout__msi_create(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        order = self.client.Order.create(self.checkout_order_object.copy())

        checkout = order.checkout
        self.assertFalse(checkout.monthly_installments_enabled)
        assert checkout.type == "Integration"
        assert checkout.status == "Issued"
        assert len(checkout.id) == 36
