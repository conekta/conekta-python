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
from conekta.api.products_api import ProductsApi  # noqa: E501
from conekta.rest import ApiException
from test.test_utils import get_base_path


class TestProductsApi(unittest.TestCase):
    """ProductsApi unit test stubs"""

    def setUp(self):
        self.api = conekta.api.products_api.ProductsApi(ApiClient(
            configuration=conekta.Configuration(host=get_base_path())
        ))  # noqa: E501

    def tearDown(self):
        pass

    def test_orders_create_product(self):
        """Test case for orders_create_product

        Create Product  # noqa: E501
        """
        accept_language = 'es'
        rq = conekta.Product(
            name='plan test',
            quantity=1,
            unit_price=1000
        )
        response = self.api.orders_create_product('ord_2tUigJ8DgBhbp6w5D', rq, accept_language)
        self.assertIsNotNone(response)

    def test_orders_delete_product(self):
        """Test case for orders_delete_product

        Delete Product  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.orders_delete_product('ord_2tUigJ8DgBhbp6w5D', 'line_item_2tVz8UkyWhSxLfUd7',
                                                  accept_language)
        self.assertIsNotNone(response)

    def test_orders_update_product(self):
        """Test case for orders_update_product

        Update Product  # noqa: E501
        """
        accept_language = 'es'
        rq = conekta.UpdateProduct(
            name='plan test',
            quantity=1,
            unit_price=1000
        )
        response = self.api.orders_update_product('ord_2tUigJ8DgBhbp6w5D', 'line_item_2tVz8UkyWhSxLfUd7', rq,
                                                  accept_language)
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
