#!/usr/bin/env python3
"""
Module to test the client module
"""
import unittest
from typing import Dict
from client import GithubOrgClient
from unittest.mock import patch, MagicMock, PropertyMock
from utils import get_json
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for the GithubOrgClient class.
    """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch('client.get_json',)
    def test_org(self, org_name, expected_data, mock_json):
        """
        Test that GithubOrgClient.org returns the expected value.
        """
        mock_json.return_value = MagicMock(return_value=expected_data)

        client = GithubOrgClient(org_name)

        result = client.org()

        mock_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}'
            )

        self.assertEqual(result, expected_data)

    def test_public_repos_url(self):
        """
        Test GithubOrgClient._public_repos_url returns the correct URL.
        """
        mocked_org_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
            }

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = mocked_org_payload

            client = GithubOrgClient("google")

            self.assertEqual(client._public_repos_url,
                             mocked_org_payload["repos_url"]
                             )
            mock_org.assert_called_once()

    @patch("client.get_json", return_value=[{"name": "Test value"}])
    def test_public_repos(self, mock_get_json):
        """
        Test GithubOrgClient.public_repos returns the expected list of repos.
        """
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/"
                          ) as pub:
            client = GithubOrgClient("Test value")
            result = client.public_repos()

            self.assertEqual(result, ["Test value"])
            mock_get_json.assert_called_once
            pub.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),
        ])
    def test_has_license(self, repo, license_key, exp_result):
        """Method to test GithubOrgClient.has_license function"""

        client = GithubOrgClient("Test value")
        result = client.has_license(repo, license_key)
        self.assertEqual(exp_result, result)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test for the GithubOrgClient class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Setup class method to mock requests.get.
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if url.endswith('/orgs/google'):
                return MagicMock(json=lambda: cls.org_payload)
            elif url.endswith('/repos'):
                return MagicMock(json=lambda: cls.repos_payload)
            elif url.endswith('/repos/apache2'):
                return MagicMock(json=lambda: cls.apache2_repos)
            else:
                raise ValueError(f"Unexpected URL: {url}")

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """
        Teardown class method to stop the patcher.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test GithubOrgClient.public_repos method for integration.
        """
        client = GithubOrgClient("google")

        repos = client.public_repos()

        self.assertEqual(repos, self.expected_repos)

        self.mock_get.assert_called_once_with(
            'https://api.github.com/orgs/google/repos'
        )

    def test_public_repos_with_license(self):
        """
        Test GithubOrgClient.public_repos method with license
        filter for integration.
        """
        client = GithubOrgClient("google")

        repos = client.public_repos(license="apache-2.0")

        self.assertEqual(repos, self.apache2_repos)
        self.mock_get.assert_called_once_with(
            'https://api.github.com/orgs/google/repos?license=apache-2.0'
        )


if __name__ == '__main__':
    unittest.main()
