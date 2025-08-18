import pytest

from apps.order_processes.infrastructure.orm_models.models import Driver


@pytest.mark.django_db
def test_driver_str():
    driver = Driver.objects.create(name="John Doe", phone="123456789", email="john@example.com")
    assert str(driver) == "John Doe"
