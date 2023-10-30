from typing import Optional

from fastapi import Request


class ViewModelBase:
    def __init__(self, request: Request) -> None:
        self.request: Request = request
        self.error: Optional[str] = None
        self.user_id: Optional[int] = None

    def to_dict_(self) -> dict:
        return self.__dict__
