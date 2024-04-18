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
from conekta.api.customers_api import CustomersApi  # noqa: E501
from conekta.rest import ApiException
from test.test_utils import get_base_path


class TestCustomersApi(unittest.TestCase):
    """CustomersApi unit test stubs"""

    def setUp(self):
        self.api = conekta.api.customers_api.CustomersApi(ApiClient(
            configuration=conekta.Configuration(host=get_base_path())
        ))  # noqa: E501

    def tearDown(self):
        pass

    def test_create_customer(self):
        """Test case for create_customer

        Create customer  # noqa: E501
        """
        accept_language = 'es'
        customer = conekta.Customer(
            email='foo@foo.com',
            name='Foo Foo',
            phone='5534343434'
        )
        response = self.api.create_customer(customer, accept_language)
        self.assertIsNotNone(response)

    def test_create_customer_fiscal_entities(self):
        """Test case for create_customer_fiscal_entities

        Create Fiscal Entity  # noqa: E501
        """
        accept_language = 'es'
        customer = conekta.CustomerFiscalEntitiesRequest(
            email='foo@foo.com',
            company_name='Foo Foo',
            phone='5534343434',
            address=conekta.CustomerAddress(
                street1='street',
                postal_code='1444',
                city='CDMX'
            )
        )
        response = self.api.create_customer_fiscal_entities('cus_2tYENskzTjjgkGQLt', customer, accept_language)
        self.assertIsNotNone(response)

    def test_delete_customer_by_id(self):
        """Test case for delete_customer_by_id

        Delete Customer  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.delete_customer_by_id('cus_2tYENskzTjjgkGQLt', accept_language)
        self.assertIsNotNone(response)

    def test_get_customer_by_id(self):
        """Test case for get_customer_by_id

        Get Customer  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.get_customer_by_id('cus_2tYENskzTjjgkGQLt', accept_language)
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_sources)
        self.assertIsNotNone(response.payment_sources.data)
        self.assertIsInstance(response.payment_sources.data[0].actual_instance, conekta.PaymentMethodCardResponse)
        self.assertEqual('card', response.payment_sources.data[0].actual_instance.type)

    def test_get_customers(self):
        """Test case for get_customers

        Get a list of customers  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.get_customers(accept_language, limit=20)
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data)
        self.assertIsNotNone(response.data[0].payment_sources)
        self.assertIsNotNone(response.data[0].payment_sources.data)
        self.assertIsInstance(response.data[0].payment_sources.data[0].actual_instance,
                              conekta.PaymentMethodSpeiRecurrent)
        self.assertEqual('spei_recurrent', response.data[0].payment_sources.data[0].actual_instance.type)

    def test_update_customer(self):
        """Test case for update_customer

        Update customer  # noqa: E501
        """
        accept_language = 'es'
        customer = conekta.UpdateCustomer(
            email='foo@foo.com'
        )
        response = self.api.update_customer('cus_2tYENskzTjjgkGQLt', customer, accept_language)
        self.assertIsNotNone(response)

    def test_update_customer_fiscal_entities(self):
        """Test case for update_customer_fiscal_entities

        Update  Fiscal Entity  # noqa: E501
        """
        accept_language = 'es'
        customer = conekta.CustomerUpdateFiscalEntitiesRequest(
            company_name='Foo Foo'
        )
        response = self.api.update_customer_fiscal_entities('cus_2tYENskzTjjgkGQLt', 'fis_ent_2tYENskzTjjgkGQLr', customer, accept_language)
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
