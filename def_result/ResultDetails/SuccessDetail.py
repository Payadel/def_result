from typing import Any, List, Optional

from def_result.ResultDetail import ResultDetail


class SuccessDetail(ResultDetail):
    """ Stores the result of a successful operation. """
    def __init__(self, title: Optional[str] = "Operation was successful",
                 message: Optional[str] = None,
                 code: Optional[int] = 200,
                 more_data: Optional[List[Any]] = None):
        super().__init__(title if title else "Operation was successful", message, code, more_data)
