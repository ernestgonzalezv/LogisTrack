import uuid
from datetime import datetime

from apps.users.domain.enums.incidence_type import IncidenceType
from apps.users.domain.enums.incidence_status import IncidenceStatus


class Incidence:
    id: uuid.UUID
    type: IncidenceType
    description: str
    date: datetime
    status: IncidenceStatus

    def __init__(self, id: uuid.UUID, type: IncidenceType, description: str, date: datetime, status: IncidenceStatus):
        self.id = id
        self.type = type
        self.description = description
        self.date = date
        self.status = status
