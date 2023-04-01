from typing import Any, List, Optional


class ResultDetail:
    """ Stores the details of a result.

    Attributes:
        title (str): A title for the result detail.
        message (str, optional): A message describing the result detail. Defaults to None.
        code (int, optional): A code associated with the result detail. Defaults to None.
        more_data (List[Any]): A list of additional data associated with the result detail. Defaults to an empty list.
    """

    title: str
    message: Optional[str]
    code: Optional[int]
    more_data: List[Any] = []

    def __init__(self, title: str,
                 message: Optional[str] = None,
                 code: Optional[int] = None,
                 more_data: Optional[List[Any]] = None):
        """ Initializes a new instance of the ResultDetail class.

        Args:
            title (str): A title for the result detail.
            message (str, optional): A message describing the result detail. Defaults to None.
            code (int, optional): A code associated with the result detail. Defaults to None.
            more_data (List[Any], optional): A list of additional data associated with the result detail. Defaults to an empty list.

        Raises:
            ValueError: If title is empty or None.
        """
        if title is None or title == '':
            raise ValueError("title is required")
        self.title = title
        self.message = message
        self.code = code
        if more_data is not None:
            self.more_data = more_data

    def is_instance_of(self, cls):
        """ Checks if the result detail is an instance of the given class.

        Args:
            cls (type): A type to check against.

        Returns:
            bool: True if the result detail is an instance of the given class, False otherwise.
        """
        return isinstance(self, cls)

    def add_more_data(self, data: Any) -> None:
        """ Adds more data to the result detail.

        Args:
            data (Any): Additional data to add to the result detail.
        """

        if data is None:
            return
        self.more_data = []
        self.more_data.append(data)

    def __str__(self):
        """ Returns a string representation of the result detail.

        Returns:
            str: A string representation of the result detail.
        """
        result: str = f"Title: {self.title}\n"

        if self.message:
            result += f"Message: {self.message}\n"
        if self.code:
            result += f"Code: {self.code}\n"

        return result
