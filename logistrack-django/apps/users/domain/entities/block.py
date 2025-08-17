import uuid
from datetime import datetime
from typing import Optional

from apps.users.domain.entities.driver import Driver


class Block:
    id: uuid.UUID
    creation_date: datetime
    driver: Optional[Driver]

    def __init__(self, id: uuid.UUID, creation_date: datetime, driver: Optional[Driver] = None):
        self.id = id
        self.creation_date = creation_date
        self.driver = driver
