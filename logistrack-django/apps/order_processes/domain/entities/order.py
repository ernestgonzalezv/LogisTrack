import uuid
from datetime import datetime
from typing import List, Optional

from apps.order_processes.domain.entities.block import Block
from apps.order_processes.domain.entities.distribution_center import DistributionCenter
from apps.order_processes.domain.entities.incidence import Incidence
from apps.order_processes.domain.entities.order_product import OrderProduct
from apps.order_processes.domain.entities.pyme import Pyme
from apps.order_processes.domain.entities.reception import Reception
from apps.order_processes.domain.enums.order_status import OrderStatus


class Order:
    id: uuid.UUID
    pyme: Pyme
    distribution_center: DistributionCenter
    dispatch_date: datetime
    status: OrderStatus
    total_weight: float
    total_volume: float
    products: List[OrderProduct]
    preparation_status: int
    distribution_status: int
    block: Optional[Block] = None,
    receptions: Optional[List[Reception]] = None
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
        preparation_status: int,
        distribution_status: int,
        block: Optional[Block] = None,
        receptions: Optional[List[Reception]] = None,
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
        self.preparation_status = preparation_status
        self.distribution_status = distribution_status
        self.block = block
        self.incidences = incidences or []
        self.receptions = receptions or []
