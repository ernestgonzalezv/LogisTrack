from typing import Optional, List

from apps.order_processes.application.core.paging.models.page_search_args_input import SortingOption, FilterOption


class PageSearchArgs:
    def __init__(
        self,
        page_index: int = 0,
        page_size: int = 20,
        sorting_options: Optional[List[SortingOption]] = None,
        filtering_options: Optional[List[FilterOption]] = None,
        paging_strategy: str = "default"
    ):
        self.page_index = page_index
        self.page_size = page_size
        self.sorting_options = sorting_options or []
        self.filtering_options = filtering_options or []
        self.paging_strategy = paging_strategy
