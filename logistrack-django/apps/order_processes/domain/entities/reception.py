import uuid
from datetime import datetime
from typing import Optional

from apps.order_processes.domain.entities.user import User


class Reception:
    id: uuid.UUID
    order_id: uuid.UUID
    user: Optional[User]
    reception_date: datetime

    def __init__(
        self,
        id: uuid.UUID,
        order_id: uuid.UUID,
        user: Optional[User],
        reception_date: datetime
    ):
        self.id = id
        self.order_id = order_id
        self.user = user
        self.reception_date = reception_date
