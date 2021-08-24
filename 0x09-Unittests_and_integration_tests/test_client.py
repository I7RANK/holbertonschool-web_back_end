#!/usr/bin/env python3
"""This module contais the test for the GithubOrgClient class
"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
import json


class TestGithubOrgClient(unittest.TestCase):
    """test for the GithubOrgClient class
    """
    @parameterized.expand([
        ('google', 'Hola'),
        ('abc', 'Hola')
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, mocked):
        """test the GithubOrgClient.org method
        """
        mocked.return_value = expected
        github_org_client = GithubOrgClient(org)

        self.assertEqual(github_org_client.org, expected)
        mocked.assert_called_once()

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_public_repos_url(self, org):
        """test the GithubOrgClient._public_repos_url method
        """
        github_org_client = GithubOrgClient(org)
        expected_url = 'https://api.github.com/orgs/{}/repos'.format(org)
        expected = {"repos_url": expected_url}

        prop = 'client.GithubOrgClient.org'
        with patch(prop, new_callable=PropertyMock) as mocked:
            mocked.return_value = expected
            value = expected["repos_url"]
            self.assertEqual(github_org_client._public_repos_url, value)
