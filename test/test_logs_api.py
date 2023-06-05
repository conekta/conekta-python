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
from conekta.api.logs_api import LogsApi  # noqa: E501
from conekta.rest import ApiException
from test.test_utils import get_base_path


class TestLogsApi(unittest.TestCase):
    """LogsApi unit test stubs"""

    def setUp(self):
        self.api = conekta.api.logs_api.LogsApi(ApiClient(
            configuration=conekta.Configuration(host=get_base_path())
        ))  # noqa: E501

    def tearDown(self):
        pass

    def test_get_log_by_id(self):
        """Test case for get_log_by_id

        Get Log  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.get_log_by_id('6419dd15b985080001fc280e', accept_language)
        self.assertIsNotNone(response)

    def test_get_logs(self):
        """Test case for get_logs

        Get List Of Logs  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.get_logs(accept_language, limit=20)
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
