from math import ceil
from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")

class QueryResult(Generic[T]):
    def __init__(
        self,
        items: List[T],
        page_index: int = 0,
        page_size: int = 10,
        total_count: Optional[int] = None,
        error: Optional[str] = None
    ):
        self.error = error
        self.PageIndex = max(0, page_index)
        self.PageSize = min(max(0, page_size), 100)
        self.TotalCount = total_count if total_count is not None else len(items)
        self.TotalPages = ceil(self.TotalCount / self.PageSize) if self.PageSize > 0 else 0
        self.HasPrevious = self.PageIndex > 0
        self.HasNext = self.PageIndex < (self.TotalPages - 1)
        self.Data = items

    @property
    def has_error(self) -> bool:
        return self.error is not None