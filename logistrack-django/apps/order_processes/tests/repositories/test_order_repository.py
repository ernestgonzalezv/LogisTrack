import pytest
import uuid
from datetime import datetime, timedelta

from apps.order_processes.application.core.paging.models.page_search_args_input import FilterOption, SortingOption
from apps.order_processes.domain.enums.incidence_status import IncidenceStatus
from apps.order_processes.domain.enums.incidence_type import IncidenceType
from apps.order_processes.infrastructure.repositories.order_repository import OrderRepository
from apps.order_processes.application.core.paging.models.page_search_args import PageSearchArgs
from apps.order_processes.infrastructure.orm_models.models import (
    Order as OrderModel,
    Pyme as PymeModel,
    DistributionCenter as DCModel,
    Product as ProductModel,
    OrderProduct as OrderProductModel, Incidence, BlockOrder, Driver, Block,
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


@pytest.mark.django_db
def test_order_repository_filter_by_status():
    repo = OrderRepository()
    pyme = PymeModel.objects.create(id=uuid.uuid4(), name="Pyme", city="X")
    dc = DCModel.objects.create(id=uuid.uuid4(), name="DC", city="Y")
    o1 = OrderModel.objects.create(id=uuid.uuid4(), pyme=pyme, distribution_center=dc,
                                   dispatch_date=datetime.now(),
                                   status=OrderStatus.DISPATCHED.value,
                                   total_weight=1, total_volume=1)
    page_args = PageSearchArgs(
        page_index=0, page_size=10,
        filtering_options=[FilterOption(field="status", value=f"{OrderStatus.DISPATCHED.value}")]
    )
    result = repo.get_orders_by_stage(page_args)
    assert any(o.status == OrderStatus.DISPATCHED for o in result.Data)

@pytest.mark.django_db
def test_order_repository_pagination_has_next_and_previous():
    repo = OrderRepository()
    pyme = PymeModel.objects.create(id=uuid.uuid4(), name="Pyme", city="X")
    dc = DCModel.objects.create(id=uuid.uuid4(), name="DC", city="Y")
    for i in range(15):
        OrderModel.objects.create(id=uuid.uuid4(), pyme=pyme, distribution_center=dc,
                                  dispatch_date=datetime.now(),
                                  status=OrderStatus.PREPARATION.value,
                                  total_weight=1, total_volume=1)
    # Página 0
    result_page0 = repo.get_orders_by_stage(PageSearchArgs(page_index=0, page_size=10))
    assert result_page0.HasNext is True
    assert result_page0.HasPrevious is False
    # Página 1
    result_page1 = repo.get_orders_by_stage(PageSearchArgs(page_index=1, page_size=10))
    assert result_page1.HasNext is False
    assert result_page1.HasPrevious is True

@pytest.mark.django_db
def test_order_repository_sorting():
    repo = OrderRepository()
    pyme = PymeModel.objects.create(id=uuid.uuid4(), name="Pyme", city="X")
    dc = DCModel.objects.create(id=uuid.uuid4(), name="DC", city="Y")
    OrderModel.objects.create(id=uuid.uuid4(), pyme=pyme, distribution_center=dc,
                              dispatch_date=datetime(2024,1,1),
                              status=OrderStatus.PREPARATION.value,
                              total_weight=1, total_volume=1)
    OrderModel.objects.create(id=uuid.uuid4(), pyme=pyme, distribution_center=dc,
                              dispatch_date=datetime(2025,1,1),
                              status=OrderStatus.PREPARATION.value,
                              total_weight=1, total_volume=1)
    page_args = PageSearchArgs(
        page_index=0, page_size=10,
        sorting_options=[SortingOption(field="dispatch_date", direction="desc")]
    )
    result = repo.get_orders_by_stage(page_args)
    assert result.Data[0].dispatch_date.year == 2025

def test_order_repository_handles_error(monkeypatch):
    repo = OrderRepository()
    # forzar excepción en map_orders
    monkeypatch.setattr("apps.order_processes.infrastructure.repositories.order_repository.map_orders",
                        lambda *args, **kwargs: 1/0)
    page_args = PageSearchArgs(page_index=0, page_size=10)
    result = repo.get_orders_by_stage(page_args)
    assert result.error is not None
    assert result.Data == []

@pytest.mark.django_db
def test_order_repository_filter_by_distribution_center_name():
    repo = OrderRepository()
    pyme = PymeModel.objects.create(id=uuid.uuid4(), name="P1", city="X")
    dc = DCModel.objects.create(id=uuid.uuid4(), name="MainDC", city="Y")
    OrderModel.objects.create(
        id=uuid.uuid4(), pyme=pyme, distribution_center=dc,
        dispatch_date=datetime.now(), status=OrderStatus.PREPARATION.value,
        total_weight=1, total_volume=1
    )
    page_args = PageSearchArgs(
        page_index=0, page_size=10,
        filtering_options=[FilterOption(field="distribution_center_name", value="Main")]
    )
    result = repo.get_orders_by_stage(page_args)
    assert all("Main" in o.distribution_center.name for o in result.Data)



@pytest.mark.django_db
def test_order_repository_filter_by_dispatch_date_range():
    repo = OrderRepository()
    pyme = PymeModel.objects.create(id=uuid.uuid4(), name="P1", city="X")
    dc = DCModel.objects.create(id=uuid.uuid4(), name="DC1", city="Y")

    order = OrderModel.objects.create(
        id=uuid.uuid4(), pyme=pyme, distribution_center=dc,
        dispatch_date=datetime(2025, 1, 1),
        status=OrderStatus.PREPARATION.value, total_weight=1, total_volume=1
    )

    # rango incluye el 1 de enero 2025
    page_args = PageSearchArgs(
        page_index=0, page_size=10,
        filtering_options=[
            FilterOption(field="dispatch_date_start", value=datetime(2024, 12, 31)),
            FilterOption(field="dispatch_date_end", value=datetime(2025, 1, 2)),
        ]
    )
    result = repo.get_orders_by_stage(page_args)
    assert any(o.id == order.id for o in result.Data)


@pytest.mark.django_db
def test_order_repository_filter_with_unknown_field(capfd):
    repo = OrderRepository()
    pyme = PymeModel.objects.create(id=uuid.uuid4(), name="P1", city="X")
    dc = DCModel.objects.create(id=uuid.uuid4(), name="DC1", city="Y")
    OrderModel.objects.create(
        id=uuid.uuid4(), pyme=pyme, distribution_center=dc,
        dispatch_date=datetime.now(), status=OrderStatus.PREPARATION.value,
        total_weight=1, total_volume=1
    )

    page_args = PageSearchArgs(
        page_index=0, page_size=10,
        filtering_options=[FilterOption(field="unknown_field", value="???")]
    )
    result = repo.get_orders_by_stage(page_args)
    # No debe romperse
    assert result.error is None
    out, _ = capfd.readouterr()
    assert "unknown field" in out


@pytest.mark.django_db
def test_order_repository_sorting_ignores_unknown_field():
    repo = OrderRepository()
    pyme = PymeModel.objects.create(id=uuid.uuid4(), name="P1", city="X")
    dc = DCModel.objects.create(id=uuid.uuid4(), name="DC1", city="Y")
    o1 = OrderModel.objects.create(
        id=uuid.uuid4(), pyme=pyme, distribution_center=dc,
        dispatch_date=datetime(2024, 1, 1), status=OrderStatus.PREPARATION.value,
        total_weight=1, total_volume=1
    )
    o2 = OrderModel.objects.create(
        id=uuid.uuid4(), pyme=pyme, distribution_center=dc,
        dispatch_date=datetime(2025, 1, 1), status=OrderStatus.PREPARATION.value,
        total_weight=1, total_volume=1
    )

    page_args = PageSearchArgs(
        page_index=0, page_size=10,
        sorting_options=[SortingOption(field="status", direction="asc")]
    )
    result = repo.get_orders_by_stage(page_args)
    # Como "status" no es un campo soportado en order_by, el orden no se modifica
    ids = [o.id for o in result.Data]
    assert set(ids) == {o1.id, o2.id}