import uuid
from datetime import datetime

from apps.order_processes.application.features.orders.models.output.orders_output_model import PymeOutputModel, \
    DistributionCenterOutputModel, ProductOutputModel, DriverOutputModel, BlockOutputModel, IncidenceOutputModel, \
    OrderOutputModel
from apps.order_processes.domain.enums.incidence_status import IncidenceStatus
from apps.order_processes.domain.enums.incidence_type import IncidenceType
from apps.order_processes.domain.enums.order_status import OrderStatus


def test_output_models_creation_and_status_name():
    pyme = PymeOutputModel(id=uuid.uuid4(), name="Pyme1", city="City1")
    dc = DistributionCenterOutputModel(id=uuid.uuid4(), name="DC1", city="City1")
    product = ProductOutputModel(id=uuid.uuid4(), sku="SKU1", name="Prod1", description="Desc", quantity=5)
    driver = DriverOutputModel(id=uuid.uuid4(), name="Driver1", phone="123", email="a@b.com")
    block = BlockOutputModel(id=uuid.uuid4(), creation_date=datetime.now(), driver=driver)
    incidence = IncidenceOutputModel(
        id=uuid.uuid4(),
        type=IncidenceType.DAMAGED,
        description="Test incidence",
        date=datetime.now(),
        status=IncidenceStatus.OPEN
    )

    order = OrderOutputModel(
        id=uuid.uuid4(),
        pyme=pyme,
        distribution_center=dc,
        dispatch_date=datetime.now(),
        status=OrderStatus.DELIVERED,
        total_weight=10.0,
        total_volume=20.0,
        products=[product],
        block=block,
        incidences=[incidence],
        distribution_status=0,
        preparation_status=0
    )

    # Validar atributos
    assert order.pyme.name == "Pyme1"
    assert order.distribution_center.name == "DC1"
    assert order.products[0].quantity == 5
    assert order.block.driver.name == "Driver1"
    assert order.incidences[0].description == "Test incidence"

    # Validar status_name
    assert order.status_name == "DELIVERED"
    assert order.distribution_status == 0
    assert order.preparation_status == 0

    # Validar que incidences por defecto sea lista vacía si no se pasa
    order2 = OrderOutputModel(
        id=uuid.uuid4(),
        pyme=pyme,
        distribution_center=dc,
        dispatch_date=datetime.now(),
        status=OrderStatus.DELIVERED,
        total_weight=1.0,
        total_volume=2.0,
        distribution_status=0,
        preparation_status=0,
        products=[]
    )
    assert order2.incidences == []
