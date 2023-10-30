from fastapi import Request

from viewmodels.shared.viewmodel import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request) -> None:
        super().__init__(request)

        self.release_count: int = 1
        self.user_count: int = 2
        self.package_count: int = 3
        self.packages_list: list = []
