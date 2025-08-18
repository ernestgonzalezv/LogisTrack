import pytest
from django.utils import timezone

from apps.order_processes.domain.enums.order_status import OrderStatus
from apps.order_processes.infrastructure.orm_models.models import Driver, Block, Pyme, DistributionCenter, Order, \
    BlockOrder


@pytest.mark.django_db
def test_block_order_creation():
    driver = Driver.objects.create(name="John Doe", phone="123456789", email="john@example.com")
    block = Block.objects.create(driver=driver)
    pyme = Pyme.objects.create(name="Pyme Test", city="Havana")
    dc = DistributionCenter.objects.create(name="DC Test", city="Havana")
    order = Order.objects.create(
        pyme=pyme,
        distribution_center=dc,
        dispatch_date=timezone.now(),
        status=OrderStatus.DELIVERED.value,
        total_weight=10.5,
        total_volume=20.0
    )
    bo = BlockOrder.objects.create(block=block, order=order)
    assert bo.block.id == block.id
    assert bo.order.id == order.id
