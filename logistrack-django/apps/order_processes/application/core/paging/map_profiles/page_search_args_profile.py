from apps.order_processes.application.core.paging.models.page_search_args import PageSearchArgs
from apps.order_processes.application.core.paging.models.page_search_args_input import PageSearchArgsInput


class PageSearchArgsMapper:
    """
    Perfil de mapeo para convertir PageSearchArgsInput (DTO) a PageSearchArgs (Domain)
    """

    @staticmethod
    def input_to_domain(input_model: PageSearchArgsInput) -> PageSearchArgs:
        return PageSearchArgs(
            page_index=input_model.page_index,
            page_size=input_model.page_size,
            sorting_options=input_model.sorting_options,
            filtering_options=input_model.filtering_options,
            paging_strategy=input_model.paging_strategy
        )
