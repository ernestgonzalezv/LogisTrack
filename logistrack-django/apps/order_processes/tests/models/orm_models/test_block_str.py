import pytest

from apps.order_processes.infrastructure.orm_models.models import Driver, Block


@pytest.mark.django_db
def test_block_str():
    driver = Driver.objects.create(name="John Doe", phone="123456789", email="john@example.com")
    block = Block.objects.create(driver=driver)
    assert str(block).startswith("Block ")
