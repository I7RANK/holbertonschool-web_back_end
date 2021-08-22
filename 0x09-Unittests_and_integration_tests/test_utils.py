#!/usr/bin/env python3
"""This module contais the test for the utils class
"""

import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """test class for utils.access_nested_map method"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping, path: Sequence,
        expected: Any
    ):
        """test for utils.access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
