from datetime import datetime

import pytest

from apps.order_processes.domain.enums.order_status import OrderStatus
from apps.order_processes.infrastructure.map_profiles.order_mapper import map_order
from apps.order_processes.infrastructure.orm_models.models import Pyme, DistributionCenter, Order as InfraOrder


@pytest.mark.django_db
def test_map_order_basic():
    pyme = Pyme.objects.create(name="Pyme1", city="City1")
    dc = DistributionCenter.objects.create(name="DC1", city="City1")
    order = InfraOrder.objects.create(
        pyme=pyme,
        distribution_center=dc,
        dispatch_date=datetime.now(),
        status=OrderStatus.DELIVERED.value,
        total_weight=10,
        total_volume=20
    )
    mapped = map_order(order)
    assert mapped.id == order.id
    assert mapped.pyme.name == "Pyme1"
    assert mapped.distribution_center.name == "DC1"
    assert mapped.products == []
    assert mapped.incidences == []
    assert mapped.block is None
