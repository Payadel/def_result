from typing import Any, Optional

from def_result.ResultDetail import ResultDetail


class Result:
    success: bool
    detail: Optional[ResultDetail] = None
    value: Optional[Any] = None

    def __init__(self, success: bool, detail: Optional[ResultDetail] = None, value: Optional[Any] = None):
        self.success = success
        self.detail = detail
        self.value = value

    @staticmethod
    def ok(value: Optional[Any] = None, detail: Optional[ResultDetail] = None):
        return Result(True, detail=detail, value=value)

    @staticmethod
    def fail(detail: Optional[ResultDetail] = None):
        return Result(False, detail)

    def code(self, default_success_code: int = 200, default_error_code: int = 500) -> int:
        if self.detail and self.detail.code:
            return self.detail.code
        return default_success_code if self.success else default_error_code
