from datetime import datetime

import pytest

from apps.order_processes.domain.enums.order_status import OrderStatus
from apps.order_processes.infrastructure.map_profiles.order_mapper import map_orders
from apps.order_processes.infrastructure.orm_models.models import Pyme, DistributionCenter, Order as InfraOrder


@pytest.mark.django_db
def test_map_orders_list():
    pyme = Pyme.objects.create(name="Pyme5", city="City5")
    dc = DistributionCenter.objects.create(name="DC5", city="City5")
    order1 = InfraOrder.objects.create(
        pyme=pyme,
        distribution_center=dc,
        dispatch_date=datetime.now(),
        status=OrderStatus.DELIVERED.value,
        total_weight=1,
        total_volume=2
    )
    order2 = InfraOrder.objects.create(
        pyme=pyme,
        distribution_center=dc,
        dispatch_date=datetime.now(),
        status=OrderStatus.DELIVERED.value,
        total_weight=3,
        total_volume=4
    )

    mapped_list = map_orders([order1, order2])
    assert len(mapped_list) == 2
    assert mapped_list[0].id == order1.id
    assert mapped_list[1].id == order2.id
