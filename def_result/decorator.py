from def_result.Result import Result
from def_result.ResultDetails.Errors.ExceptionError import ExceptionError


def def_result(func):
    """
    A decorator function that wraps the return value of a function with a `Result`
    object containing additional information such as success status and error messages.

    Args:
        func: The function to be wrapped.

    Returns:
        A new function that wraps the return value of `func` in a `Result` object.
    """
    def wrapper(*args, **kwargs):
        try:
            result_value = func(*args, **kwargs)
            if isinstance(result_value, Result):
                return result_value
            result = Result.ok(value=result_value)
        except Exception as e:
            result = Result.fail(detail=ExceptionError(message=str(e), exception=e))
        return result

    return wrapper
