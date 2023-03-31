import unittest

from def_result.Result import Result
from def_result.ResultDetail import ResultDetail


class TestResult(unittest.TestCase):
    def test_init_without_optional_args(self):
        result = Result(True)

        self.assertTrue(result.success)
        self.assertIsNone(result.detail)
        self.assertIsNone(result.value)

    def test_init_with_optional_args(self):
        value = 123
        result = Result(success=True, detail=ResultDetail(title="test"), value=value)

        self.assertTrue(result.success)
        self.assertTrue(isinstance(result.detail, ResultDetail))
        self.assertEqual(result.value, value)

    def test_ok_without_optional_args(self):
        result = Result.ok()

        self.assertTrue(result.success)
        self.assertIsNone(result.detail)
        self.assertIsNone(result.value)

    def test_ok_with_optional_args(self):
        value = 123
        result = Result.ok(detail=ResultDetail(title="test"), value=value)

        self.assertTrue(result.success)
        self.assertTrue(isinstance(result.detail, ResultDetail))
        self.assertEqual(result.value, value)

    def test_fail_without_optional_args(self):
        result = Result.fail()

        self.assertFalse(result.success)
        self.assertIsNone(result.detail)
        self.assertIsNone(result.value)

    def test_fail_with_optional_args(self):
        result = Result.fail(detail=ResultDetail(title="test"))

        self.assertFalse(result.success)
        self.assertTrue(isinstance(result.detail, ResultDetail))
        self.assertIsNone(result.value)

    def test_code_without_detail_and_without_args(self):
        # Success
        result = Result.ok()
        self.assertEqual(result.code(), 200)

        # Fail
        result = Result.fail()
        self.assertEqual(result.code(), 500)

    def test_code_without_detail_and_with_args(self):
        # Success
        result = Result.ok()
        self.assertEqual(result.code(default_success_code=0, default_error_code=1), 0)

        # Fail
        result = Result.fail()
        self.assertEqual(result.code(default_success_code=0, default_error_code=1), 1)

    def test_code_with_detail_and_without_args(self):
        detail = ResultDetail(title="test", code=100)
        # Success
        result = Result.ok(detail=detail)
        self.assertEqual(result.code(), 100)

        # Fail
        result = Result.fail(detail=detail)
        self.assertEqual(result.code(), 100)

    def test_code_with_detail_and_with_args(self):
        detail = ResultDetail(title="test", code=100)
        # Success
        result = Result.ok(detail=detail)
        self.assertEqual(result.code(default_success_code=0, default_error_code=1), 100)

        # Fail
        result = Result.fail(detail=detail)
        self.assertEqual(result.code(default_success_code=0, default_error_code=1), 100)


if __name__ == "__main__":
    unittest.main()
