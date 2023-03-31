import unittest
from typing import Any, List

from def_result.ResultDetail import ResultDetail


def assert_more_data(test_class: unittest.TestCase, result_detail: ResultDetail, data: List[Any]):
    """ A helper function to test more_data field """
    test_class.assertIsNotNone(result_detail.more_data)  # It should never be None.

    test_class.assertEqual(len(result_detail.more_data), len(data))

    for index, item in enumerate(data):
        test_class.assertEqual(result_detail.more_data[index], item)
