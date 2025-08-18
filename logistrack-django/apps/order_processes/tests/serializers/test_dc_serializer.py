import uuid

import pytest

from apps.order_processes.domain.entities.distribution_center import DistributionCenter
from apps.order_processes.presentation.serializers.orders.orders_serializer import \
    DistributionCenterOutputModelSerializer


@pytest.mark.django_db
def test_distribution_center_serializer():
    dc = DistributionCenter(id=uuid.uuid4(), name="DC Test", city="La Habana")
    serializer = DistributionCenterOutputModelSerializer(dc)
    data = serializer.data
    assert data["name"] == "DC Test"
    assert data["city"] == "La Habana"
