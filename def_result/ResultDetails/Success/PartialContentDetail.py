from typing import Any, List, Optional

from def_result.ResultDetails.SuccessDetail import SuccessDetail


class PartialContentDetail(SuccessDetail):
    """ Partial content """

    def __init__(self, title: Optional[str] = "Partial content",
                 message: Optional[str] = None,
                 code: Optional[int] = 206,
                 more_data: Optional[List[Any]] = None):
        super().__init__(title=title, message=message, code=code, more_data=more_data)
