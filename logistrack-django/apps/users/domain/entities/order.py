import uuid
from datetime import datetime
from typing import List, Optional

from apps.users.domain.entities.block import Block
from apps.users.domain.entities.distribution_center import DistributionCenter
from apps.users.domain.entities.incidence import Incidence
from apps.users.domain.entities.order_product import OrderProduct
from apps.users.domain.entities.pyme import Pyme
from apps.users.domain.enums.order_status import OrderStatus


class Order:
    id: uuid.UUID
    pyme: Pyme
    distribution_center: DistributionCenter
    dispatch_date: datetime
    status: OrderStatus
    total_weight: float
    total_volume: float
    products: List[OrderProduct]
    block: Optional[Block] = None
    incidences: Optional[List[Incidence]] = None

    def __init__(
        self,
        id: uuid.UUID,
        pyme: Pyme,
        distribution_center: DistributionCenter,
        dispatch_date: datetime,
        status: OrderStatus,
        total_weight: float,
        total_volume: float,
        products: List[OrderProduct],
        block: Optional[Block] = None,
        incidences: Optional[List[Incidence]] = None
    ):
        self.id = id
        self.pyme = pyme
        self.distribution_center = distribution_center
        self.dispatch_date = dispatch_date
        self.status = status
        self.total_weight = total_weight
        self.total_volume = total_volume
        self.products = products
        self.block = block
        self.incidences = incidences or []
