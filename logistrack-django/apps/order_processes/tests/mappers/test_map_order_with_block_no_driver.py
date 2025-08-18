from datetime import datetime

import pytest

from apps.order_processes.domain.enums.order_status import OrderStatus
from apps.order_processes.infrastructure.map_profiles.order_mapper import map_order
from apps.order_processes.infrastructure.orm_models.models import Pyme, DistributionCenter, Block, Order as InfraOrder, \
    BlockOrder


@pytest.mark.django_db
def test_map_order_with_block_no_driver():
    pyme = Pyme.objects.create(name="Pyme3", city="City3")
    dc = DistributionCenter.objects.create(name="DC3", city="City3")
    block = Block.objects.create(driver=None)
    order = InfraOrder.objects.create(
        pyme=pyme,
        distribution_center=dc,
        dispatch_date=datetime.now(),
        status=OrderStatus.DELIVERED.value,
        total_weight=5,
        total_volume=10
    )
    BlockOrder.objects.create(block=block, order=order)

    mapped = map_order(order)
    assert mapped.block is not None
    assert mapped.block.driver is None
