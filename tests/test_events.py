#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>
#(c) 2014- Leo Fischer / Conekta <@leofischer/@conektaio>

from . import BaseEndpointTestCase

class OrdersEndpointTestCase(BaseEndpointTestCase):

    def test_01_order_event(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        order = self.client.Order.create(self.order_object.copy())
        event = order.events()

        assert event.data


    def test_02_line_item_event(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        raw_order["charges"] = None
        order = self.client.Order.create(raw_order)

        line_item = order.line_items[0]
        line_item.update(self.line_item_object.copy())

        event = order.line_items[0].events()

        assert event.total
        assert event.object

    def test_03_tax_line_event(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        raw_order["charges"] = None
        order = self.client.Order.create(raw_order)

        tax_line = order.tax_lines[0]
        tax_line.update(self.tax_line_object.copy())

        event = order.tax_lines[0].events()

        assert event.total
        assert event.object

    def test_04_shipping_lines_event(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        raw_order["charges"] = None
        order = self.client.Order.create(raw_order)

        shipping_line = order.shipping_lines[0]
        shipping_line.update(self.shipping_lines_object.copy())

        event = order.shipping_lines[0].events()

        assert event.total
        assert event.object

    def test_05_discount_lines_event(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        raw_order["charges"] = None
        order = self.client.Order.create(raw_order)

        discount_line = order.discount_lines[0]
        discount_line.update(self.discount_line_object.copy())

        event = order.discount_lines[0].events()

        assert event.total
        assert event.object

    def test_06_discount_lines_event(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        raw_order["charges"] = None
        order = self.client.Order.create(raw_order)

        discount_line = order.discount_lines[0]
        discount_line.update(self.discount_line_object.copy())

        event = order.discount_lines[0].events()

        assert event.total
        assert event.object

    def test_07_customer_event(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        customer = self.client.Customer.create(self.customer_object.copy())

        event = customer.events()

        assert event.data

    def test_08_customer_payment_source_event(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        customer = self.client.Customer.create(self.customer_object.copy())
        payment_source = customer.payment_sources[0]
        payment_source.update(self.update_payment_source_object.copy())
        event = customer.payment_sources[0].events()

        assert event.total
        assert event.object

    def test_09_customer_shipping_contact_event(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        customer = self.client.Customer.create(self.customer_object.copy())
        shipping_contact = customer.shipping_contacts[0]
        shipping_contact.update(self.shipping_contact_object.copy())
        event = customer.shipping_contacts[0].events()

        assert event.total
        assert event.object
