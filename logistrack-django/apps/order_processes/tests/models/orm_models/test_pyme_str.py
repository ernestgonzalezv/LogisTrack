import pytest

from apps.order_processes.infrastructure.orm_models.models import Pyme


@pytest.mark.django_db
def test_pyme_str():
    pyme = Pyme.objects.create(name="Pyme Test", city="Havana")
    assert str(pyme) == "Pyme Test"
