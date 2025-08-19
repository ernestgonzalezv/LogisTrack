import pytest
from apps.order_processes.domain.repositories.order_repository import IOrderRepository

def test_iorderrepository_is_abstract():
    # No se puede instanciar sin implementar el método abstracto
    with pytest.raises(TypeError):
        IOrderRepository()

def test_iorderrepository_subclass_must_implement():
    # Creamos una subclase dummy sin implementación -> debe fallar
    class BadRepo(IOrderRepository):
        pass

    with pytest.raises(TypeError):
        BadRepo()

def test_iorderrepository_subclass_ok():
    # Subclase con implementación válida -> se puede instanciar
    class GoodRepo(IOrderRepository):
        def get_orders_by_stage(self, page_args):
            return "fake result"

    repo = GoodRepo()
    assert repo.get_orders_by_stage(None) == "fake result"
