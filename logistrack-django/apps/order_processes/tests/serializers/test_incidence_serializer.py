import uuid

import pytest
from django.utils import timezone

from apps.order_processes.presentation.serializers.orders.orders_serializer import IncidenceOutputModelSerializer


@pytest.mark.django_db
def test_incidence_serializer():
    incidence_data = {
        "id": str(uuid.uuid4()),
        "type": 1,
        "description": "Roto en transporte",
        "date": timezone.now(),
        "status": 0,
    }
    serializer = IncidenceOutputModelSerializer(incidence_data)
    data = serializer.data
    assert data["description"] == "Roto en transporte"
    assert data["status"] == 0