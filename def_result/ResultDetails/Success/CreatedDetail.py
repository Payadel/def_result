from typing import Any, List, Optional

from def_result.ResultDetails.SuccessDetail import SuccessDetail


class CreatedDetail(SuccessDetail):
    """ A new resource has been created """
    def __init__(self, title: Optional[str] = "A new resource has been created",
                 message: Optional[str] = None,
                 code: Optional[int] = 201,
                 more_data: Optional[List[Any]] = None):
        super().__init__(title=title, message=message, code=code, more_data=more_data)
