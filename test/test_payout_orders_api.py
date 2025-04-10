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

from conekta.api.payout_orders_api import PayoutOrdersApi


class TestPayoutOrdersApi(unittest.TestCase):
    """PayoutOrdersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PayoutOrdersApi()

    def tearDown(self) -> None:
        pass

    def test_cancel_payout_order_by_id(self) -> None:
        """Test case for cancel_payout_order_by_id

        Cancel Payout Order
        """
        pass

    def test_create_payout_order(self) -> None:
        """Test case for create_payout_order

        Create payout order
        """
        pass

    def test_get_payout_order_by_id(self) -> None:
        """Test case for get_payout_order_by_id

        Get Payout Order
        """
        pass

    def test_get_payout_orders(self) -> None:
        """Test case for get_payout_orders

        Get a list of Payout Orders
        """
        pass


if __name__ == '__main__':
    unittest.main()
