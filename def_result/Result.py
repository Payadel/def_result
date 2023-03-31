from typing import Any, Optional

from def_result.ResultDetail import ResultDetail


class Result:
    """ Stores the result of a function.

    Attributes:
        success (bool): A flag indicating whether the result was successful.
        detail (ResultDetail, optional): The details of the result. Defaults to None.
        value (Any, optional): The value of the result. Defaults to None.
    """
    success: bool
    detail: Optional[ResultDetail] = None
    value: Optional[Any] = None

    def __init__(self, success: bool, detail: Optional[ResultDetail] = None, value: Optional[Any] = None):
        self.success = success
        self.detail = detail
        self.value = value

    @staticmethod
    def ok(value: Optional[Any] = None, detail: Optional[ResultDetail] = None):
        """ Returns a successful result.

        Args:
            value (Any, optional): The value of the result. Defaults to None.
            detail (ResultDetail, optional): The details of the result. Defaults to None.

        Returns:
            Result: A successful result.
        """
        return Result(True, detail=detail, value=value)

    @staticmethod
    def fail(detail: Optional[ResultDetail] = None):
        """ Returns a failed result.

        Args:
            detail (ResultDetail, optional): The details of the result. Defaults to None.

        Returns:
            Result: A failed result.
        """
        return Result(False, detail)

    def code(self, default_success_code: int = 200, default_error_code: int = 500) -> int:
        """ Returns the result code.

        Args:
            default_success_code (int, optional): The default success code. Defaults to 200.
            default_error_code (int, optional): The default error code. Defaults to 500.

        Returns:
            int: The result code.
        """
        if self.detail and self.detail.code:
            return self.detail.code
        return default_success_code if self.success else default_error_code
