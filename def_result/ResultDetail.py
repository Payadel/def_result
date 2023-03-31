from typing import Any, List, Optional


class ResultDetail:
    title: str
    message: Optional[str]
    code: Optional[int]
    more_data: List[Any] = []

    def __init__(self, title: str,
                 message: Optional[str] = None,
                 code: Optional[int] = None,
                 more_data: Optional[List[Any]] = None):
        if not title:
            raise ValueError("title is required")
        self.title = title
        self.message = message
        self.code = code
        if more_data is not None:
            self.more_data = more_data

    def is_instance_of(self, cls):
        return isinstance(self, cls)

    def add_more_data(self, data: Any) -> None:
        if not data:
            return
        if not self.more_data:
            self.more_data = []
        self.more_data.append(data)

    def __str__(self):
        result: str = ""

        if self.title:
            result += f"Title: {self.title}\n"
        if self.message:
            result += f"Message: {self.message}\n"
        if self.code:
            result += f"Code: {self.code}\n"

        return result
