#!/usr/bin/env python3
"""a test module for utils.py
"""
from unittest.mock import patch, Mock
from typing import Dict
from utils import get_json, memoize
import unittest
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Test cases for the access_nested_map function. """
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access_nest_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test for KeyError raised for missing keys"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """ Test Class for the utils.get_json function. """
    @patch('utils.requests.get')
    def test_get_json(self, mock_get: Mock) -> None:
        """method to test utils.get_json"""
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]

        for test_url, test_payload in test_cases:
            # configure the mock to return a Mock object with a json method
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)

            self.assertEqual(result, test_payload)

            mock_get.reset_mock()

    class TestMemoize(unittest.TestCase):
        """Test cases for the memoize decorator."""
        def test_memoize(self):
            """Test that memoize decorator caches results."""
            class TestClass:
                """Class that defines attributes to test memoize"""
                def a_method(self):
                    """Method that returns an instance of memoize class"""
                    return 42

                @memoize
                def a_property(self):
                    """Method that defines a property instance of memoize"""

                    return self.a_method()

            test_instance = TestClass()
            with patch.object(test_instance, 'a_method',
                              return_value=42) as mock_a_method:

                result1 = test_instance.a_property
                result2 = test_instance.a_property

                mock_a_method.assert_called_once()

                self.assertEqual(result1, result2)


if __name__ == '__main__':
    unittest.main()
