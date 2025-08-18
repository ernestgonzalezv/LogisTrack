import pytest
import uuid
from datetime import datetime
from unittest.mock import MagicMock

from apps.order_processes.application.core.paging.models.query_result import QueryResult
from apps.order_processes.application.core.paging.models.page_search_args_input import PageSearchArgsInput
from apps.order_processes.application.features.orders.handler.orders_query_handler import BlockProcessesQueryHandler
from apps.order_processes.application.features.orders.queries.get_orders_query import GetOrdersQuery
from apps.order_processes.application.core.paging.models.paged_response import PagedResponse

from apps.order_processes.domain.entities.order import Order
from apps.order_processes.domain.entities.pyme import Pyme
from apps.order_processes.domain.entities.distribution_center import DistributionCenter
from apps.order_processes.domain.entities.product import Product
from apps.order_processes.domain.entities.order_product import OrderProduct
from apps.order_processes.domain.enums.order_status import OrderStatus


@pytest.mark.django_db
def test_handler_returns_paged_response_success():
    # Arrange
    mock_repo = MagicMock()

    # Crear objetos de dominio reales
    pyme = Pyme(id=uuid.uuid4(), name="Pyme Test", city="La Habana")
    dc = DistributionCenter(id=uuid.uuid4(), name="DC Test", city="La Habana")
    product = Product(id=uuid.uuid4(), sku="SKU123", name="Producto Test", description="Producto Test")
    order_product = OrderProduct(product=product, quantity=10)

    order1 = Order(
        id=uuid.uuid4(),
        pyme=pyme,
        distribution_center=dc,
        dispatch_date=datetime.now(),
        status=OrderStatus.PREPARATION,
        total_weight=100.0,
        total_volume=50.0,
        products=[order_product],
    )

    order2 = Order(
        id=uuid.uuid4(),
        pyme=pyme,
        distribution_center=dc,
        dispatch_date=datetime.now(),
        status=OrderStatus.DISPATCHED,
        total_weight=200.0,
        total_volume=80.0,
        products=[order_product],
    )

    # Mock del repositorio devuelve QueryResult con Orders
    mock_repo.get_orders_by_stage.return_value = QueryResult(
        items=[order1, order2],
        page_index=1,
        page_size=2,
        total_count=50,
        error=None
    )

    handler = BlockProcessesQueryHandler(mock_repo)
    page_args = PageSearchArgsInput(page_index=1, page_size=2)
    query = GetOrdersQuery(page_args=page_args)

    # Act
    result: PagedResponse = handler.handle(query)

    # Assert
    assert isinstance(result, PagedResponse)
    assert result.success is True
    assert len(result.data) == 2
    assert result.total_count == 50
    assert result.page_index == 1
    assert result.page_size == 2
    assert result.has_next is True
    assert result.has_previous is True


@pytest.mark.django_db
def test_handler_returns_empty_paged_response():
    # Arrange
    mock_repo = MagicMock()

    # Mock del repositorio devuelve QueryResult vacío
    mock_repo.get_orders_by_stage.return_value = QueryResult(
        items=[],
        page_index=0,
        page_size=10,
        total_count=0,
        error=None
    )

    handler = BlockProcessesQueryHandler(mock_repo)
    page_args = PageSearchArgsInput(page_index=0, page_size=10)
    query = GetOrdersQuery(page_args=page_args)

    # Act
    result: PagedResponse = handler.handle(query)

    # Assert
    assert isinstance(result, PagedResponse)
    assert result.success is True
    assert result.data == []
    assert result.total_count == 0
    assert result.page_index == 0
    assert result.page_size == 10
    assert result.has_next is False
    assert result.has_previous is False

