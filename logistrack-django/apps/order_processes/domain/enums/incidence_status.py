from enum import IntEnum


class IncidenceStatus(IntEnum):
    OPEN = 1
    IN_PROGRESS = 2
    RESOLVED = 3
    CLOSED = 4
