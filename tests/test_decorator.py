import unittest

from def_result.decorator import def_result
from def_result.Result import Result
from def_result.ResultDetails.Errors.BadRequestError import BadRequestError
from tests.helpers import assert_result, assert_result_detail


def divide_numbers(a: int, b: int):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def divide_numbers_support_result(a: int, b: int) -> Result:
    if b == 0:
        return Result.fail(BadRequestError(message="Cannot divide by zero"))
    return Result.ok(a / b)


class TestDefResultDecorator(unittest.TestCase):
    def test_def_result_on_simple_function_ok(self):
        # Test that the decorator returns a Result object with ok status when the function runs successfully
        decorated_function = def_result(divide_numbers)
        result = decorated_function(10, 2)

        assert_result(test_class=self, result=result, success=True, value=5)

    def test_def_result_on_simple_function_error(self):
        # Test that the decorator returns a Result object with error status and ExceptionError detail when
        # the function raises an exception
        self.assertRaises(ValueError, divide_numbers, 10, 0)

        decorated_function = def_result(divide_numbers)
        result = decorated_function(10, 0)

        assert_result(test_class=self, result=result, success=False, detail=result.detail)
        assert_result_detail(test_class=self, result_detail=result.detail, title="An exception occurred",
                             message="Cannot divide by zero", code=500)

    def test_def_result_on_result_function_ok(self):
        decorated_function = def_result(divide_numbers_support_result)
        result = decorated_function(10, 2)

        assert_result(test_class=self, result=result, success=True, value=5)

    def test_def_result_on_result_function_error(self):
        decorated_function = def_result(divide_numbers_support_result)
        result = decorated_function(10, 0)

        assert_result(test_class=self, result=result, success=False, detail=result.detail)
        assert_result_detail(test_class=self, result_detail=result.detail, title="BadRequest Error",
                             message="Cannot divide by zero", code=400)


if __name__ == '__main__':
    unittest.main()
