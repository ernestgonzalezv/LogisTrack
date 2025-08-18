from datetime import datetime

import pytest

from apps.order_processes.domain.enums.order_status import OrderStatus
from apps.order_processes.infrastructure.map_profiles.order_mapper import map_order
from apps.order_processes.infrastructure.orm_models.models import Pyme, DistributionCenter, Driver, Block, \
    Order as InfraOrder, BlockOrder


@pytest.mark.django_db
def test_map_order_with_block_and_driver():
    pyme = Pyme.objects.create(name="Pyme2", city="City2")
    dc = DistributionCenter.objects.create(name="DC2", city="City2")
    driver = Driver.objects.create(name="Driver1", phone="123", email="a@b.com")
    block = Block.objects.create(driver=driver)
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
    assert mapped.block.driver.name == "Driver1"
