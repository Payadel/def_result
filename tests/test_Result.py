import unittest

from def_result.Result import Result
from def_result.ResultDetail import ResultDetail
from tests.helpers import assert_result


class TestResult(unittest.TestCase):
    def test_init_without_optional_args(self):
        result = Result(True)

        assert_result(self, result=result, success=True)

    def test_init_with_optional_args(self):
        detail = ResultDetail(title="test")
        value = 123
        result = Result(success=True, detail=detail, value=value)

        assert_result(self, result=result, success=True, detail=detail, value=value)

    def test_ok_without_optional_args(self):
        result = Result.ok()

        assert_result(self, result=result, success=True)

    def test_ok_with_optional_args(self):
        value = 123
        detail = ResultDetail(title="test")
        result = Result.ok(detail=detail, value=value)

        assert_result(self, result=result, success=True, detail=detail, value=value)

    def test_fail_without_optional_args(self):
        result = Result.fail()

        assert_result(self, result=result, success=False)

    def test_fail_with_optional_args(self):
        detail = ResultDetail(title="test")
        result = Result.fail(detail=detail)

        assert_result(self, result=result, success=False, detail=detail)

    def test_code_without_detail_and_without_args(self):
        # Success
        result = Result.ok()
        self.assertEqual(200, result.code())

        # Fail
        result = Result.fail()
        self.assertEqual(500, result.code())

    def test_code_without_detail_and_with_args(self):
        # Success
        result = Result.ok()
        self.assertEqual(0, result.code(default_success_code=0, default_error_code=1))

        # Fail
        result = Result.fail()
        self.assertEqual(1, result.code(default_success_code=0, default_error_code=1))

    def test_code_with_detail_and_without_args(self):
        detail = ResultDetail(title="test", code=100)
        # Success
        result = Result.ok(detail=detail)
        self.assertEqual(100, result.code())

        # Fail
        result = Result.fail(detail=detail)
        self.assertEqual(100, result.code())

    def test_code_with_detail_and_with_args(self):
        detail = ResultDetail(title="test", code=100)
        # Success
        result = Result.ok(detail=detail)
        self.assertEqual(100, result.code(default_success_code=0, default_error_code=1))

        # Fail
        result = Result.fail(detail=detail)
        self.assertEqual(100, result.code(default_success_code=0, default_error_code=1))


if __name__ == "__main__":
    unittest.main()
