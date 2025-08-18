import uuid

import pytest

from apps.order_processes.domain.entities.pyme import Pyme
from apps.order_processes.presentation.serializers.orders.orders_serializer import PymeOutputModelSerializer


@pytest.mark.django_db
def test_pyme_serializer():
    pyme = Pyme(id=uuid.uuid4(), name="Pyme Test", city="La Habana")
    serializer = PymeOutputModelSerializer(pyme)
    data = serializer.data
    assert data["name"] == "Pyme Test"
    assert data["city"] == "La Habana"
