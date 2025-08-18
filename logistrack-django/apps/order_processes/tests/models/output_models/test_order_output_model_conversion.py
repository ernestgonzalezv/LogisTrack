import uuid
from datetime import datetime

import pytest

from apps.order_processes.application.features.orders.models.output.orders_output_model import \
    DistributionCenterOutputModel, PymeOutputModel, DriverOutputModel, OrderOutputModel
from apps.order_processes.domain.enums.order_status import OrderStatus


@pytest.mark.django_db
def test_order_output_model_conversion():
    pyme_in = DistributionCenterOutputModel(id=uuid.uuid4(), name="PymeOut", city="CityX")
    pyme_out = PymeOutputModel(id=uuid.uuid4(), name="PymeOut", city="CityX")
    driver_out = DriverOutputModel(id=uuid.uuid4(), name="DriverOut", phone="123", email="a@b.com")
    order_out = OrderOutputModel(
        id=uuid.uuid4(),
        pyme=pyme_out,
        distribution_center=pyme_in,
        dispatch_date=datetime.now(),
        status=OrderStatus.DELIVERED,
        total_weight=1.0,
        total_volume=2.0,
        products=[],
        block=None,
        incidences=None
    )
    assert order_out.status_name == "DELIVERED"
    assert order_out.incidences == []
