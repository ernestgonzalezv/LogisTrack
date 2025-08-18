import uuid

import pytest

from apps.order_processes.presentation.serializers.orders.orders_serializer import DriverOutputModelSerializer


@pytest.mark.django_db
def test_driver_serializer():
    driver_data = {
        "id": str(uuid.uuid4()),
        "name": "Juan Pérez",
        "phone": "555-1234",
        "email": "juan@test.com",
    }
    serializer = DriverOutputModelSerializer(driver_data)
    data = serializer.data
    assert data["name"] == "Juan Pérez"
    assert data["email"] == "juan@test.com"