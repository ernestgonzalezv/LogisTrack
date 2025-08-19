from datetime import datetime

import pytest

from apps.order_processes.domain.enums.incidence_status import IncidenceStatus
from apps.order_processes.domain.enums.incidence_type import IncidenceType
from apps.order_processes.domain.enums.order_status import OrderStatus
from apps.order_processes.infrastructure.map_profiles.order_mapper import map_order
from apps.order_processes.infrastructure.orm_models.models import Pyme, DistributionCenter, Order as InfraOrder, \
    Product, OrderProduct, Incidence


@pytest.mark.django_db
def test_map_order_with_products_and_incidences():
    pyme = Pyme.objects.create(name="Pyme4", city="City4")
    dc = DistributionCenter.objects.create(name="DC4", city="City4")
    order = InfraOrder.objects.create(
        pyme=pyme,
        distribution_center=dc,
        dispatch_date=datetime.now(),
        status=OrderStatus.DELIVERED.value,
        total_weight=5,
        total_volume=10
    )
    product = Product.objects.create(sku="SKU1", name="Product1", description="Desc")
    OrderProduct.objects.create(order=order, product=product, quantity=2)
    inc = Incidence.objects.create(
        order=order,
        type=IncidenceType.DAMAGED.value,
        description="Test incidence",
        date=datetime.now(),
        status=IncidenceStatus.OPEN.value
    )

    mapped = map_order(order)
    assert len(mapped.products) == 1
    assert mapped.products[0].quantity == 2
    assert len(mapped.incidences) == 1
    assert mapped.incidences[0].description == "Test incidence"
