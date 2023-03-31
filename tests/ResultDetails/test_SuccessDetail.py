import unittest

from def_result.ResultDetails.SuccessDetail import SuccessDetail
from tests.helpers import assert_more_data


class TestSuccessDetail(unittest.TestCase):
    def test_init_without_args(self):
        success_detail = SuccessDetail()

        self.assertEqual(success_detail.title, "Operation was successful")
        self.assertIsNone(success_detail.message)
        self.assertEqual(success_detail.code, 200)
        assert_more_data(self, success_detail, [])

    def test_init_with_args(self):
        success_detail = SuccessDetail(title="title", message="message", code=100, more_data=["message"])

        self.assertEqual(success_detail.title, "title")
        self.assertEqual(success_detail.message, "message")
        self.assertEqual(success_detail.code, 100)
        assert_more_data(self, success_detail, ["message"])


if __name__ == '__main__':
    unittest.main()
