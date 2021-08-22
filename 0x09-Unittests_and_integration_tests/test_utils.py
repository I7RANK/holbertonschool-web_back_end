#!/usr/bin/env python3
"""This module contais the test for the utils class
"""

import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """test class for utils.access_nested_map method"""
    @parameterized.expand([
        ('expected_1', {"a": 1}, ("a",), 1),
        ('expected_dict', {"a": {"b": 2}}, ("a",), {"b": 2}),
        ('expected_2', {"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, name, nested_map, path, expected):
        """test for utils.access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
