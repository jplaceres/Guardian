# coding: utf-8

"""
    Betaface API 2.0

    Betaface face recognition API.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.admin_api import AdminApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.admin_api.AdminApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v2_admin_usage_get(self):
        """Test case for v2_admin_usage_get

        get API usage information. (Administrative endpoint - API secret required)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
