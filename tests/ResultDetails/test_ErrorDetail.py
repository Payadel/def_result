import unittest

from def_result.ResultDetails.ErrorDetail import ErrorDetail
from tests.helpers import assert_error_detail


class TestErrorDetail(unittest.TestCase):
    def test_init_without_args(self):
        error_detail = ErrorDetail()

        assert_error_detail(test_class=self, error_detail=error_detail, title="An error occurred", code=500)

    def test_init_with_args(self):
        exception = Exception("Fake exception")
        error_detail = ErrorDetail(title="title", message="message", code=100, errors={"message": "error"},
                                   exception=exception, more_data=["more_data"])

        assert_error_detail(test_class=self, error_detail=error_detail, title="title", message="message", code=100,
                            errors={"message": "error"}, exception=exception, more_data=["more_data"])

    def test_add_or_update_error(self):
        error_detail = ErrorDetail()
        self.assertEqual(None, error_detail.errors)
        # Add an error
        error_detail.add_or_update_error("key", "error")
        self.assertEqual({"key": "error"}, error_detail.errors)
        # Update an error
        error_detail.add_or_update_error("key", "error2")
        self.assertEqual({"key": "error2"}, error_detail.errors)
        print(str(error_detail))

    def test_str(self):
        error_detail = ErrorDetail(title="title", message="message", code=100, errors={"message": "error"},
                                   exception=Exception("Fake exception"), more_data=["more_data"])
        self.assertTrue(str(error_detail).startswith(
            "Title: title\nMessage: message\nCode: 100\nErrors: {'message': 'error'}\nException: Fake exception\nStack trace:"))

        error_detail = ErrorDetail(title="title", message="message", code=100,
                                   exception=Exception("Fake exception"), more_data=["more_data"])
        self.assertTrue(str(error_detail).startswith(
            "Title: title\nMessage: message\nCode: 100\nException: Fake exception\nStack trace:"))

        error_detail = ErrorDetail(title="title", message="message", code=100, more_data=["more_data"])
        self.assertTrue(str(error_detail).startswith(
            "Title: title\nMessage: message\nCode: 100\nStack trace:"))


if __name__ == '__main__':
    unittest.main()
