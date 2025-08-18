import uuid

import pytest
from django.utils import timezone

from apps.order_processes.presentation.serializers.orders.orders_serializer import BlockOutputModelSerializer


@pytest.mark.django_db
def test_block_serializer_with_driver():
    driver_data = {
        "id": str(uuid.uuid4()),
        "name": "Chofer Test",
        "phone": "555-4321",
        "email": "chofer@test.com",
    }
    block_data = {
        "id": str(uuid.uuid4()),
        "creation_date": timezone.now(),
        "driver": driver_data,
    }
    serializer = BlockOutputModelSerializer(block_data)
    data = serializer.data
    assert data["driver"]["name"] == "Chofer Test"