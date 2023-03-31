from typing import Any, Dict, List, Optional

from def_result.ResultDetails.ErrorDetail import ErrorDetail


class UnauthorizedError(ErrorDetail):
    """ An error that occurs when a user is not authorized to perform a certain action.

    This error is a subclass of `ErrorDetail`, which provides additional details about the error.

    Args:
        title (str, optional): A title for the error. Defaults to "Unauthorized Error".
        message (str, optional): A message describing the error. Defaults to None.
        code (int, optional): An error code associated with the error. Defaults to 401.
        errors (Dict[str, str], optional): A dictionary containing additional error details. Defaults to None.
        exception (Exception, optional): An exception that caused the error. Defaults to None.
        more_data (List[Any], optional): A list of additional data associated with the error. Defaults to None.
    """

    def __init__(self, title: Optional[str] = "Unauthorized Error",
                 message: Optional[str] = None,
                 code: Optional[int] = 401,
                 errors: Optional[Dict[str, str]] = None,
                 exception: Optional[Exception] = None,
                 more_data: Optional[List[Any]] = None):
        super().__init__(title=title, message=message, code=code, errors=errors, exception=exception,
                         more_data=more_data)
