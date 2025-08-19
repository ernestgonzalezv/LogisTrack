import pytest
from django.utils import timezone

from apps.order_processes.domain.enums.order_status import OrderStatus
from apps.order_processes.infrastructure.orm_models.models import Pyme, DistributionCenter, Order, Product, OrderProduct


@pytest.mark.django_db
def test_order_product_creation():
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
    product = Product.objects.create(sku="SKU123", name="Product Test", description="Desc")
    op = OrderProduct.objects.create(order=order, product=product, quantity=5)
    assert op.quantity == 5
    assert op.order.id == order.id
    assert op.product.id == product.id
