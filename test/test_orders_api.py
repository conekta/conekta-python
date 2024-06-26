# coding: utf-8

"""
    Conekta API

    Conekta sdk  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: engineering@conekta.com
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import unittest

import conekta
from conekta import ApiClient
from conekta.rest import ApiException
from test.test_utils import get_base_path
from conekta.models.order_response_charges import OrderResponseCharges
from conekta.models.order_response import OrderResponse
from conekta.api.orders_api import OrdersApi
from conekta.models.payment_method_cash import PaymentMethodCash

class TestOrdersApi(unittest.TestCase):
    """OrdersApi unit test stubs"""

    def setUp(self):
        self.api = OrdersApi(ApiClient(
            configuration=conekta.Configuration(host=get_base_path(),access_token='key_xxxx')
        ))  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_order(self):
        """Test case for cancel_order

        Cancel Order  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.cancel_order('ord_2tqaGQYZyvBsMKEgs', accept_language)
        self.assertIsNotNone(response)

    def test_create_order(self):
        """Test case for create_order

        Create order  # noqa: E501
        """
        accept_language = 'es'
        rq = conekta.OrderRequest(
            currency='MXN',
            customer_info=conekta.OrderRequestCustomerInfo(
                oneof_schema_2_validator=conekta.CustomerInfoJustCustomerId(
                    customer_id='cus_2tYENskzTjjgkGQLt'
                )
            ),
            line_items=[conekta.Product(
                name='product',
                quantity=1,
                unit_price=1000
            )],
            shipping_contact=conekta.CustomerShippingContacts(
                address=conekta.CustomerShippingContactsAddress(
                        street1='Calle 123, int 2',
                        street2='Col. Condesa',
                        city='Cuauhtémoc',
                        state='Ciudad de México',
                        country='MX',
                    ),
                metadata={}
                ),
            fiscal_entity=conekta.OrderFiscalEntityRequest(
                address=conekta.FiscalEntityAddress(
                        state='Ciudad de México',
                        street1='Calle 123, int 2',
                        street2='Col. Condesa',
                        city='Cuauhtémoc',
                        country='MX',
                        postal_code='06100',
                        external_number='123',
                    ),
                metadata={},
            )
        )
        response = self.api.create_order(rq, accept_language)
        
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.charges)
        self.assertIsInstance(response.charges, OrderResponseCharges)
        self.assertIsInstance(response, OrderResponse)
        self.assertEqual('list', response.charges.object)
        self.assertEqual(1, len(response.charges.data))
        self.assertIsInstance(response.charges.data[0].payment_method.actual_instance, PaymentMethodCash)
        self.assertEqual("oxxo", response.charges.data[0].payment_method.actual_instance.type)

    def test_get_order_by_id(self):
        """Test case for get_order_by_id

        Get Order  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.get_order_by_id('ord_2tUigJ8DgBhbp6w5D', accept_language)
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.charges)
        self.assertIsNotNone(response.charges.data)
        charge = response.charges.data[0]
        self.assertIsNotNone(charge.payment_method)
        self.assertIsInstance(charge.payment_method.actual_instance, conekta.PaymentMethodBankTransfer)
        self.assertEqual('spei', charge.payment_method.actual_instance.type)

    def test_get_orders(self):
        """Test case for get_orders

        Get a list of Orders  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.get_orders(accept_language, limit=20)
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data)
        self.assertIsNotNone(response.data)
        self.assertIsNotNone(response.data[0].charges)
        self.assertIsNotNone(response.data[0].charges.data)
        charge = response.data[0].charges.data[0]
        self.assertIsNotNone(charge.payment_method)
        self.assertIsInstance(charge.payment_method.actual_instance, conekta.PaymentMethodCard)
        self.assertEqual('credit', charge.payment_method.actual_instance.type)

    def test_order_cancel_refund(self):
        """Test case for order_cancel_refund

        Cancel Refund  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.order_cancel_refund('ord_2tV52JvSom2w3E8bX', '6407b5bee1329a000175ba11', accept_language)
        self.assertIsNotNone(response)

    def test_order_refund(self):
        """Test case for order_refund

        Refund Order  # noqa: E501
        """
        accept_language = 'es'
        rq = conekta.OrderRefundRequest(
            amount=2000,
            reason='promo'
        )
        response = self.api.order_refund('ord_2tV52JvSom2w3E8bX', rq, accept_language)
        self.assertIsNotNone(response)

    def test_orders_create_capture(self):
        """Test case for orders_create_capture

        Capture Order  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.orders_create_capture('ord_2tV52JvSom2w3E8bX', accept_language)
        self.assertIsNotNone(response)

    def test_update_order(self):
        """Test case for update_order

        Update Order  # noqa: E501
        """
        accept_language = 'es'
        rq = conekta.OrderUpdateRequest(
            currency='MXN'
        )
        response = self.api.update_order('ord_2tV52JvSom2w3E8bX', rq, accept_language)
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
