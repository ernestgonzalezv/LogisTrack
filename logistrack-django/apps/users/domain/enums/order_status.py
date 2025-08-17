from enum import IntEnum


class OrderStatus(IntEnum):
    PREPARATION = 1
    DISPATCHED = 2
    EXPEDITION = 3
    RECEIVED = 4
    CONSOLIDATED = 5
    DELIVERED = 6


