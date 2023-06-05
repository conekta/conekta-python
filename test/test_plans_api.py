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
from conekta.api.plans_api import PlansApi  # noqa: E501
from conekta.rest import ApiException


class TestPlansApi(unittest.TestCase):
    """PlansApi unit test stubs"""

    def setUp(self):
        self.api = conekta.api.plans_api.PlansApi(ApiClient(
            configuration=conekta.Configuration(host='http://localhost:3000')
        ))  # noqa: E501

    def tearDown(self):
        pass

    def test_create_plan(self):
        """Test case for create_plan

        Create Plan  # noqa: E501
        """
        accept_language = 'es'
        rq = conekta.PlanRequest(
            amount=1000,
            currency='MXN',
            frequency=1,
            interval='week',
            name='plan test'
        )
        response = self.api.create_plan(rq, accept_language)
        self.assertIsNotNone(response)

    def test_delete_plan(self):
        """Test case for delete_plan

        Delete Plan  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.delete_plan('plan_2tZb5q8Z3PYpg6SJd', accept_language)
        self.assertIsNotNone(response)

    def test_get_plan(self):
        """Test case for get_plan

        Get Plan  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.get_plan('plan_2tZb5q8Z3PYpg6SJd', accept_language)
        self.assertIsNotNone(response)

    def test_get_plans(self):
        """Test case for get_plans

        Get A List of Plans  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.get_plans(accept_language, limit=20)
        self.assertIsNotNone(response)

    def test_update_plan(self):
        """Test case for update_plan

        Update Plan  # noqa: E501
        """
        accept_language = 'es'
        rq = conekta.PlanUpdateRequest(
            amount=1000
        )
        response = self.api.update_plan('plan_2tZb5q8Z3PYpg6SJd', rq, accept_language)
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
