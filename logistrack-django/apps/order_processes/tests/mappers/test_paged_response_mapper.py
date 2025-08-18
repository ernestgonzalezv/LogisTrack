import pytest
from apps.order_processes.application.core.paging.map_profiles.paged_response_mapper import PagedResponseMapper
from apps.order_processes.application.core.paging.models.paged_response import PagedResponse
from apps.order_processes.application.core.paging.models.query_result import QueryResult

# -------------------
# Helpers
# -------------------
def sample_mapper(x: int) -> str:
    return f"Item-{x}"

# -------------------
# Tests PagedResponseMapper
# -------------------
def test_from_query_result_with_error():
    qr = QueryResult[int](
        items=[],
        page_index=1,
        page_size=10,
        total_count=0,
        error="Some error"
    )
    result = PagedResponseMapper.from_query_result(qr, sample_mapper)
    assert isinstance(result, PagedResponse)
    assert result.success is False
    assert result.data == []
    assert result.page_index == 1
    assert result.page_size == 10
    assert result.total_count == 0
    assert result.message == "Some error"

def test_from_query_result_no_error():
    qr = QueryResult[int](
        items=[1, 2, 3],
        page_index=2,
        page_size=5,
        total_count=3,
        error=None
    )
    result = PagedResponseMapper.from_query_result(qr, sample_mapper)
    assert isinstance(result, PagedResponse)
    assert result.success is True  # Por defecto, PagedResponse success=True
    assert result.data == ["Item-1", "Item-2", "Item-3"]
    assert result.page_index == 2
    assert result.page_size == 5
    assert result.total_count == 3
    assert result.message == ""  # Por defecto no hay mensaje
