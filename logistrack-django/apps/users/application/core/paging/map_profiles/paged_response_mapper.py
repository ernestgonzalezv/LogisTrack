from typing import TypeVar, Callable
from apps.users.application.core.paging.models.paged_response import PagedResponse
from apps.users.application.core.paging.models.query_result import QueryResult

T = TypeVar("T")
U = TypeVar("U")

class PagedResponseMapper:

    @staticmethod
    def from_query_result(query_result: QueryResult[T], mapper_func: Callable[[T], U]) -> PagedResponse[U]:
        if query_result.has_error:
            return PagedResponse(
                data=[],
                success=False,
                page_index=query_result.PageIndex,
                page_size=query_result.PageSize,
                total_count=0,
                message=query_result.error
            )
        mapped_items = [mapper_func(i) for i in query_result.Data]
        return PagedResponse(
            data=mapped_items,
            page_index=query_result.PageIndex,
            page_size=query_result.PageSize,
            total_count=query_result.TotalCount
        )

