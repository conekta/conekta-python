#!/usr/bin/python
#coding: utf-8
#(c) 2017 Ramses Carbajal <@RamsesCarbajal>

from . import BaseEndpointTestCase

class OrdersEndpointTestCase(BaseEndpointTestCase):

    def test_01_order_create(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        order = self.client.Order.create(self.order_object.copy())
        assert order.currency
        line_item = order.line_items[0]
        assert line_item.name == "Box of Cohiba S1s"
        tax_line = order.tax_lines[0]
        assert tax_line.description == "IVA"
        shipping_line = order.shipping_lines[0]
        assert shipping_line.tracking_number == "TRACK123"
        discount_lines = order.discount_lines[0]
        assert discount_lines.code == "descuento"
        assert order.customer_info.name == "John Constantine"
        assert order.shipping_contact.receiver == "Marvin Fuller"
        charge = order.charges[0]
        assert charge.payment_method.service_name == "OxxoPay"
        assert charge.amount == 20000

    def test_02_order_create_line_item(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        raw_order["charges"] = None
        order = self.client.Order.create(raw_order)
        line_item = order.createLineItem(self.line_item_object.copy())
        assert line_item.name == "test line item"
        assert line_item.unit_price == 10000

    def test_03_order_create_tax_item(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        raw_order["charges"] = None
        order = self.client.Order.create(raw_order)
        tax_line = order.createTaxLine(self.tax_line_object.copy())
        assert tax_line.description == "IVA2"
        assert tax_line.amount == 600

    def test_04_order_create_shipping_line(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        raw_order["charges"] = None
        order = self.client.Order.create(raw_order)
        shipping_line = order.createShippingLine(self.shipping_lines_object.copy())
        assert shipping_line.tracking_number == "TRACK123"

    def test_05_order_create_discount_line(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        raw_order["charges"] = None
        order = self.client.Order.create(raw_order)
        discount_line = order.createDiscountLine(self.discount_line_object.copy())
        assert discount_line.code == "descuento"
        assert discount_line.amount == 100

    def test_06_order_create_shipping_contact(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        raw_order["charges"] = None
        del raw_order["shipping_contact"]
        order = self.client.Order.create(raw_order)
        shipping_contact = order.createShippingContact(self.order_shipping_contact_object.copy())
        assert shipping_contact.phone == "+525511223399"

    def test_07_order_create_charge(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        del raw_order["charges"]
        order = self.client.Order.create(raw_order)
        charge = order.charge(self.charge_object)
        assert charge.object == "charge"
        assert charge.status == "pending_payment"

    def test_08_order_update_line_item(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        del raw_order["charges"]
        order = self.client.Order.create(raw_order)
        line_item = order.line_items[0]
        raw_line_item = self.line_item_object.copy()
        del raw_line_item["tags"]
        del raw_line_item["type"]
        raw_line_item["unit_price"] = 30000
        raw_line_item["description"] = "some description"
        line_item.update(raw_line_item)
        line_item = order.line_items[0]
        assert line_item.unit_price == 30000
        assert line_item.description == "some description"

    def test_09_order_get_all_line_items(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'

        large_order_by_find  = self.client.Order.find('ord_2h9umNjHAzx8ZMtPA')
        large_order_by_where = self.client.Order.where({'id':'ord_2h9umNjHAzx8ZMtPA'})

        assert len(large_order_by_where.data[0].line_items) == 15
        assert len(large_order_by_find.line_items) == 15

    def test_10_order_update_tax_line(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        del raw_order["charges"]
        order = self.client.Order.create(raw_order)
        tax_line = order.tax_lines[0]
        raw_tax_line = self.tax_line_object.copy()
        raw_tax_line["description"] = "newIva"
        raw_tax_line["amount"] = 321
        tax_line.update(raw_tax_line)
        valid_tax_line = order.tax_lines[0]
        assert valid_tax_line.description == "newIva"
        assert valid_tax_line.amount == 321

    def test_11_order_update_shipping_line(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        del raw_order["charges"]
        order = self.client.Order.create(raw_order)
        shipping_line = order.shipping_lines[0]
        raw_shipping_line = self.shipping_lines_object.copy()
        raw_shipping_line["tracking_number"] = "fake track number"
        raw_shipping_line["amount"] = 321
        shipping_line.update(raw_shipping_line)
        shipping_line = order.shipping_lines[0]
        assert shipping_line.tracking_number == "fake track number"

    def test_12_order_update_discount_line(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        del raw_order["charges"]
        order = self.client.Order.create(raw_order)
        discount_line = order.discount_lines[0]
        raw_discount_line = self.discount_line_object.copy()
        raw_discount_line["code"] = "promocion"
        discount_line.update(raw_discount_line)
        discount_line = order.discount_lines[0]
        assert discount_line.code == "promocion"

    def test_13_order_with_token_id(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        charge = {}
        charge["payment_method"] = {}
        charge["payment_method"]["type"] = "card"
        charge["payment_method"]["token_id"] = "tok_test_visa_4242"
        raw_order["charges"] = [charge]

        order = self.client.Order.create(raw_order)
        charge = order.charges[0]
        assert charge.status == "paid"
        assert charge.amount == 20000

    def test_14_order_capture(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        charge = {}
        charge["payment_method"] = {}
        charge["payment_method"]["type"] = "card"
        charge["payment_method"]["token_id"] = "tok_test_visa_4242"
        raw_order["charges"] = [charge]
        raw_order["pre_authorize"] = True
        order = self.client.Order.create(raw_order)

        assert order.charges[0].amount == 20000
        assert order.charges[0].status == "pre_authorized"
        assert order.payment_status == "pre_authorized"

        capture_param = {}
        order.capture(capture_param)
        charge = order.charges[0]

        assert charge.amount == 20000
        assert charge.status == "paid"
        assert order.payment_status == "paid"

    def test_15_order_refund(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        charge = {}
        charge["payment_method"] = {}
        charge["payment_method"]["type"] = "card"
        charge["payment_method"]["token_id"] = "tok_test_visa_4242"
        raw_order["charges"] = [charge]

        order = self.client.Order.create(raw_order)
        order_refund_params = {}

        order_refund_params["reason"] = "requested_by_client"
        order_refund_params["amount"] = 20000

        refunded_order = order.refund(order_refund_params)

        assert refunded_order.payment_status == "refunded"

    def test_15_order_void(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        charge = {}
        charge["payment_method"] = {}
        charge["payment_method"]["type"] = "card"
        charge["payment_method"]["token_id"] = "tok_test_visa_4242"
        raw_order["charges"] = [charge]
        raw_order["pre_authorize"] = True
        order = self.client.Order.create(raw_order)

        assert order.charges[0].amount == 20000
        assert order.charges[0].status == "pre_authorized"
        assert order.payment_status == "pre_authorized"

        refunded_order = order.void()
        
        assert refunded_order.payment_status == "voided"

    def test_16_order_delete_line_item(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        del raw_order["charges"]
        order = self.client.Order.create(raw_order)
        order.createLineItem(self.line_item_object.copy())
        line_item = order.line_items[0]
        line_item_deleted = line_item.delete()

        assert line_item_deleted.deleted == True

        line_item = order.line_items[0]
        assert line_item.unit_price == 10000
        assert line_item.description == "Imported From Mex."

    def test_17_order_delete_tax_line(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        del raw_order["charges"]
        order = self.client.Order.create(raw_order)
        order.createTaxLine(self.tax_line_object.copy())
        tax_line = order.tax_lines[0]
        tax_line_deleted = tax_line.delete()

        assert tax_line_deleted.deleted == True

        tax_line = order.tax_lines[0]
        assert tax_line.description == "IVA2"
        assert tax_line.amount == 600

    def test_18_order_delete_shipping_line(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        del raw_order["charges"]
        order = self.client.Order.create(raw_order)
        order.createShippingLine(self.shipping_lines_object.copy())
        shipping_line = order.shipping_lines[0]
        shipping_line_deleted = shipping_line.delete()

        assert shipping_line_deleted.deleted == True

        shipping_line = order.shipping_lines[0]
        assert shipping_line.tracking_number == "TRACK123"
        assert shipping_line.amount == 0

    def test_18_order_delete_discount_line(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        raw_order = self.order_object.copy()
        del raw_order["charges"]
        order = self.client.Order.create(raw_order)
        order.createDiscountLine(self.discount_line_object.copy())
        discount_line = order.discount_lines[0]
        discount_line_deleted = discount_line.delete()

        assert discount_line_deleted.deleted == True

        discount_line = order.discount_lines[0]
        assert discount_line.code == "descuento"
        assert discount_line.type == "loyalty"


    def test_19_order_create_with_customer_id(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        customer = self.client.Customer.create(self.customer_object.copy())
        order_params = self.order_object.copy()
        del order_params["customer_info"]
        order_params["customer_info"] = {}
        order_params["customer_info"]["customer_id"] = customer.id

        charge_params = {}
        charge_params["payment_method"] = {}
        charge_params["payment_method"]["type"] = "card"
        charge_params["payment_method"]["token_id"] = "tok_test_visa_4242"
        order_params["charges"] = [charge_params]

        del order_params["shipping_contact"]
        order = self.client.Order.create(order_params)

        charge = order.charges[0]

        assert charge.status == "paid"
        assert charge.amount == 20000
