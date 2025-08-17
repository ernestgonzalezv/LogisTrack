from typing import List, Generic, Optional, TypeVar
from math import ceil

from apps.users.application.core.response import ResponseWithData

T = TypeVar("T")
class PagedResponse(ResponseWithData[List[T]], Generic[T]):
    def __init__(
        self,
        data: List[T],
        page_index: int = 0,
        page_size: int = 10,
        total_count: Optional[int] = None,
        success: bool = True,
        message: str =  ""
    ):
        total_count_value = total_count if total_count is not None else len(data)
        total_pages = ceil(total_count_value / page_size) if total_count_value > 0 else 0
        has_previous = page_index > 0
        has_next = page_index < total_pages - 1

        super().__init__(
            success=success,
            message=message,
            data=data
        )

        self.page_index: int = max(0, page_index)
        self.page_size: int = min(max(0, page_size), 100)
        self.total_count: int = total_count_value
        self.total_pages: int = total_pages
        self.has_previous: bool = has_previous
        self.has_next: bool = has_next
