from dataclasses import dataclass
from typing import Optional, List

@dataclass
class FilterOption:
    field: str
    value: str

@dataclass
class SortingOption:
    field: str
    direction: str = "asc"

@dataclass
class PageSearchArgsInput:
    page_index: int = 0
    page_size: int = 20
    sorting_options: Optional[List[SortingOption]] = None
    filtering_options: Optional[List[FilterOption]] = None
    paging_strategy: str = "default"