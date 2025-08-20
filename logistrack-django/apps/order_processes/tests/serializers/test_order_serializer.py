import uuid

import pytest
from django.utils import timezone

from apps.order_processes.domain.entities.distribution_center import DistributionCenter
from apps.order_processes.domain.entities.order import Order
from apps.order_processes.domain.entities.pyme import Pyme
from apps.order_processes.domain.enums.order_status import OrderStatus
from apps.order_processes.presentation.serializers.orders.orders_serializer import OrderOutputModelSerializer


@pytest.mark.django_db
def test_order_serializer_empty_block():
    pyme = Pyme(id=uuid.uuid4(), name="Pyme Test", city="La Habana")
    dc = DistributionCenter(id=uuid.uuid4(), name="DC Test", city="La Habana")
    order = Order(
        id=uuid.uuid4(),
        pyme=pyme,
        distribution_center=dc,
        dispatch_date=timezone.now(),
        status=OrderStatus.DELIVERED,
        total_weight=50.0,
        total_volume=20.0,
        products=[],
        distribution_status=0,
        preparation_status=0,
        block=None,
        incidences=[]
    )
    serializer = OrderOutputModelSerializer({
        "id": str(order.id),
        "pyme": {"id": str(pyme.id), "name": pyme.name, "city": pyme.city},
        "distribution_center": {"id": str(dc.id), "name": dc.name, "city": dc.city},
        "dispatch_date": order.dispatch_date,
        "status": order.status,
        "total_weight": order.total_weight,
        "total_volume": order.total_volume,
        "products": [],
        "block": None,
        "distribution_status": 0,
        "preparation_status": 0,
        "incidences": []
    })
    data = serializer.data
    assert data["pyme"]["name"] == "Pyme Test"
    assert data["block"] is None
