import pytest
import uuid
from datetime import datetime, timedelta

from apps.order_processes.application.core.paging.models.page_search_args_input import FilterOption
from apps.order_processes.infrastructure.repositories.order_repository import OrderRepository
from apps.order_processes.application.core.paging.models.page_search_args import PageSearchArgs
from apps.order_processes.infrastructure.orm_models.models import (
    Order as OrderModel,
    Pyme as PymeModel,
    DistributionCenter as DCModel,
    Product as ProductModel,
    OrderProduct as OrderProductModel,
)
from apps.order_processes.domain.entities.order import Order
from apps.order_processes.domain.enums.order_status import OrderStatus

@pytest.mark.django_db
def test_order_repository_returns_filtered_orders():
    repo = OrderRepository()

    pyme = PymeModel.objects.create(id=uuid.uuid4(), name="Pyme Test", city="La Habana")
    dc = DCModel.objects.create(id=uuid.uuid4(), name="DC Test", city="La Habana")
    product = ProductModel.objects.create(id=uuid.uuid4(), sku="SKU123", name="Producto Test", description="Producto Test")
    order1 = OrderModel.objects.create(
        id=uuid.uuid4(),
        pyme=pyme,
        distribution_center=dc,
        dispatch_date=datetime.now(),
        status=OrderStatus.PREPARATION.value,
        total_weight=100.0,
        total_volume=50.0,
    )
    order2 = OrderModel.objects.create(
        id=uuid.uuid4(),
        pyme=pyme,
        distribution_center=dc,
        dispatch_date=datetime.now() + timedelta(days=1),
        status=OrderStatus.DISPATCHED.value,
        total_weight=200.0,
        total_volume=80.0,
    )
    OrderProductModel.objects.create(order=order1, product=product, quantity=10)
    OrderProductModel.objects.create(order=order2, product=product, quantity=5)
    page_args = PageSearchArgs(
        page_index=0,
        page_size=10,
        filtering_options=[FilterOption(field="pyme_name", value="Pyme Test")]
    )
    result = repo.get_orders_by_stage(page_args)
    assert len(result.Data) == 2
    assert all(isinstance(o, Order) for o in result.Data)
    assert all(o.pyme.name == "Pyme Test" for o in result.Data)
    assert result.PageIndex == 0
    assert result.PageSize == 10
    assert result.TotalCount == 2
    assert not result.HasPrevious
    assert not result.HasNext
    assert result.error is None

@pytest.mark.django_db
def test_order_repository_returns_empty():
    repo = OrderRepository()
    OrderModel.objects.all().delete()
    page_args = PageSearchArgs(page_index=0, page_size=10)
    result = repo.get_orders_by_stage(page_args)
    assert result.Data == []
    assert result.TotalCount == 0
    assert result.PageIndex == 0
    assert result.PageSize == 10
    assert not result.HasNext
    assert not result.HasPrevious
    assert result.error is None
