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
from conekta.api.shipping_contacts_api import ShippingContactsApi  # noqa: E501
from conekta.rest import ApiException


class TestShippingContactsApi(unittest.TestCase):
    """ShippingContactsApi unit test stubs"""

    def setUp(self):
        self.api = conekta.api.shipping_contacts_api.ShippingContactsApi(ApiClient(
            configuration=conekta.Configuration(host='http://localhost:3000')
        ))  # noqa: E501

    def tearDown(self):
        pass

    def test_create_customer_shipping_contacts(self):
        """Test case for create_customer_shipping_contacts

        Create a shipping contacts  # noqa: E501
        """
        accept_language = 'es'
        rq = conekta.CustomerShippingContacts(
            address=conekta.CustomerShippingContactsAddress(
                street1='street'
            )
        )
        response = self.api.create_customer_shipping_contacts('cus_2tYENskzTjjgkGQLt', rq, accept_language)
        self.assertIsNotNone(response)

    def test_delete_customer_shipping_contacts(self):
        """Test case for delete_customer_shipping_contacts

        Delete shipping contacts  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.delete_customer_shipping_contacts('cus_2tYENskzTjjgkGQLt', 'ship_cont_2tY2ncFSBLUaohto2',
                                                              accept_language)
        self.assertIsNotNone(response)

    def test_update_customer_shipping_contacts(self):
        """Test case for update_customer_shipping_contacts

        Update shipping contacts  # noqa: E501
        """
        accept_language = 'es'
        rq = conekta.CustomerUpdateShippingContacts(
            address=conekta.CustomerShippingContactsAddress(
                street1='street'
            )
        )
        response = self.api.update_customer_shipping_contacts('cus_2tYENskzTjjgkGQLt', 'ship_cont_2tY2ncFSBLUaohto2',
                                                              rq, accept_language)
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
