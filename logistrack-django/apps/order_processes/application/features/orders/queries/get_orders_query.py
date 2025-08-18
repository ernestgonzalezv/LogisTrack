from apps.order_processes.application.core.paging.models.page_search_args_input import PageSearchArgsInput


class GetOrdersQuery:
    def __init__(self, page_args: PageSearchArgsInput):
        self.page_args = page_args