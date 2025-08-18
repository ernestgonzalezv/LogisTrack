from apps.order_processes.application.core.paging.models.page_search_args_input import PageSearchArgsInput, FilterOption, SortingOption

def parse_pagination_from_request(data: dict) -> PageSearchArgsInput:
    """
    Extract paging and filtering arguments from request data
    and return a PageSearchArgsInput object.
    """
    page_args_data = data.get("page_args", {})
    return PageSearchArgsInput(
        page_index=page_args_data.get("page_index", 0),
        page_size=page_args_data.get("page_size", 20),
        filtering_options=[FilterOption(**f) for f in page_args_data.get("filtering_options", [])],
        sorting_options=[SortingOption(**s) for s in page_args_data.get("sorting_options", [])],
        paging_strategy=page_args_data.get("paging_strategy", "default")
    )
