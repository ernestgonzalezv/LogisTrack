import pytest

from apps.order_processes.infrastructure.orm_models.models import DistributionCenter


@pytest.mark.django_db
def test_distribution_center_str():
    dc = DistributionCenter.objects.create(name="DC Test", city="Havana")
    assert str(dc) == "DC Test"
