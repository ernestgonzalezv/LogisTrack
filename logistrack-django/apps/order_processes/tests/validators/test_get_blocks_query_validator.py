import pytest

from apps.order_processes.application.core.paging.models.page_search_args_input import PageSearchArgsInput
from apps.order_processes.application.features.orders.queries.get_orders_query import GetOrdersQuery
from apps.order_processes.application.core.paging.models.page_search_args import PageSearchArgs
from apps.order_processes.application.features.orders.validations.get_orders_query_validator import (
    validate_get_blocks_query,
)

def test_validate_query_none():
    with pytest.raises(ValueError, match="Query cannot be None"):
        validate_get_blocks_query(None)

def test_validate_query_missing_page_args():
    query = GetOrdersQuery(page_args=None)
    with pytest.raises(ValueError, match="PageSearchArgs is required"):
        validate_get_blocks_query(query)

def test_validate_query_negative_index():
    page_args = PageSearchArgsInput(page_index=-1, page_size=10)
    query = GetOrdersQuery(page_args=page_args)
    with pytest.raises(ValueError, match="page_index cannot be negative"):
        validate_get_blocks_query(query)

def test_validate_query_invalid_page_size():
    page_args = PageSearchArgsInput(page_index=0, page_size=0)
    query = GetOrdersQuery(page_args=page_args)
    with pytest.raises(ValueError, match="page_size must be greater than 0"):
        validate_get_blocks_query(query)

def test_validate_query_valid_case():
    page_args = PageSearchArgsInput(page_index=1, page_size=20)
    query = GetOrdersQuery(page_args=page_args)
    # No exception should be raised
    validate_get_blocks_query(query)
