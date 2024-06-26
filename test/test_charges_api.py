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
from conekta.api.charges_api import ChargesApi  # noqa: E501
from conekta.rest import ApiException
from test.test_utils import get_base_path


class TestChargesApi(unittest.TestCase):
    """ChargesApi unit test stubs"""

    def setUp(self):
        self.api = conekta.api.charges_api.ChargesApi(ApiClient(
            configuration=conekta.Configuration(host=get_base_path())
        ))  # noqa: E501

    def tearDown(self):
        pass

    def test_get_charges(self):
        """Test case for get_charges

        Get A List of Charges  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.get_charges(accept_language, limit=20)
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data)
        self.assertIsNotNone(response.data[0].payment_method)
        self.assertIsInstance(response.data[0].payment_method.actual_instance, conekta.PaymentMethodCash)
        self.assertEqual('oxxo', response.data[0].payment_method.actual_instance.type)

    def test_orders_create_charge(self):
        """Test case for orders_create_charge

        Create charge  # noqa: E501
        """
        accept_language = 'es'
        charge_request = conekta.ChargeRequest(
            amount=1000,
            payment_method=conekta.ChargeRequestPaymentMethod(type='card')
        )
        response = self.api.orders_create_charge('ord_2tUigJ8DgBhbp6w5D', charge_request, accept_language)
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_method)
        self.assertIsInstance(response.payment_method.actual_instance, conekta.PaymentMethodCard)
        self.assertEqual('credit', response.payment_method.actual_instance.type)


if __name__ == '__main__':
    unittest.main()
