# coding: utf-8

"""
    Conekta API

    Conekta sdk

    The version of the OpenAPI document: 2.2.0
    Contact: engineering@conekta.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from conekta.api.customers_api import CustomersApi


class TestCustomersApi(unittest.TestCase):
    """CustomersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CustomersApi()

    def tearDown(self) -> None:
        pass

    def test_create_customer(self) -> None:
        """Test case for create_customer

        Create customer
        """
        pass

    def test_create_customer_fiscal_entities(self) -> None:
        """Test case for create_customer_fiscal_entities

        Create Fiscal Entity
        """
        pass

    def test_delete_customer_by_id(self) -> None:
        """Test case for delete_customer_by_id

        Delete Customer
        """
        pass

    def test_get_customer_by_id(self) -> None:
        """Test case for get_customer_by_id

        Get Customer
        """
        pass

    def test_get_customers(self) -> None:
        """Test case for get_customers

        Get a list of customers
        """
        pass

    def test_update_customer(self) -> None:
        """Test case for update_customer

        Update customer
        """
        pass

    def test_update_customer_fiscal_entities(self) -> None:
        """Test case for update_customer_fiscal_entities

        Update  Fiscal Entity
        """
        pass


if __name__ == '__main__':
    unittest.main()
