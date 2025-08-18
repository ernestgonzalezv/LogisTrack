import pytest
from django.utils import timezone

from apps.order_processes.domain.enums.incidence_status import IncidenceStatus
from apps.order_processes.domain.enums.incidence_type import IncidenceType
from apps.order_processes.domain.enums.order_status import OrderStatus
from apps.order_processes.infrastructure.orm_models.models import Pyme, DistributionCenter, Order, Incidence


@pytest.mark.django_db
def test_incidence_str_and_creation():
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
    incidence = Incidence.objects.create(
        order=order,
        type=IncidenceType.DAMAGED.value,
        description="Test incidence",
        date=timezone.now(),
        status=IncidenceStatus.OPEN.value
    )
    assert str(incidence).startswith("Incidence ")
    assert incidence.order.id == order.id
