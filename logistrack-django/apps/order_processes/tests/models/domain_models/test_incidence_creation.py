import uuid
from datetime import datetime

from apps.order_processes.domain.entities.incidence import Incidence
from apps.order_processes.domain.enums.incidence_status import IncidenceStatus
from apps.order_processes.domain.enums.incidence_type import IncidenceType


def test_incidence_creation():
    inc_id = uuid.uuid4()
    date_now = datetime.now()
    incidence = Incidence(
        id=inc_id,
        type=IncidenceType.DAMAGED,
        description="Test incidence",
        date=date_now,
        status=IncidenceStatus.OPEN
    )

    assert incidence.id == inc_id
    assert incidence.type == IncidenceType.DAMAGED
    assert incidence.description == "Test incidence"
    assert incidence.date == date_now
    assert incidence.status == IncidenceStatus.OPEN
