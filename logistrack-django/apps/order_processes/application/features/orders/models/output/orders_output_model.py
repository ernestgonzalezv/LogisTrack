from typing import List, Optional
from datetime import datetime
import uuid
from apps.order_processes.domain.enums.order_status import OrderStatus
from apps.order_processes.domain.enums.incidence_type import IncidenceType
from apps.order_processes.domain.enums.incidence_status import IncidenceStatus


class PymeOutputModel:
    id: str
    name: str
    city: str

    def __init__(self, id: uuid.UUID, name: str, city: str):
        self.id = str(id)
        self.name = name
        self.city = city


class DistributionCenterOutputModel:
    id: str
    name: str
    city: str

    def __init__(self, id: uuid.UUID, name: str, city: str):
        self.id = str(id)
        self.name = name
        self.city = city


class ProductOutputModel:
    id: str
    sku: str
    name: str
    description: str
    quantity: int

    def __init__(self, id: uuid.UUID, sku: str, name: str, description: str, quantity: int):
        self.id = str(id)
        self.sku = sku
        self.name = name
        self.description = description
        self.quantity = quantity


class DriverOutputModel:
    id: str
    name: str
    phone: str
    email: str

    def __init__(self, id: uuid.UUID, name: str, phone: str, email: str):
        self.id = str(id)
        self.name = name
        self.phone = phone
        self.email = email


class BlockOutputModel:
    id: str
    creation_date: str
    driver: Optional[DriverOutputModel] = None

    def __init__(self, id: uuid.UUID, creation_date: datetime, driver: Optional[DriverOutputModel] = None):
        self.id = str(id)
        self.creation_date = creation_date.isoformat()
        self.driver = driver


class IncidenceOutputModel:
    id: str
    type: int
    description: str
    date: str
    status: int

    def __init__(self, id: uuid.UUID, type: IncidenceType, description: str, date: datetime, status: IncidenceStatus):
        self.id = str(id)
        self.type = type.value
        self.description = description
        self.date = date.isoformat()
        self.status = status.value


class UserOutputModel:
    id: str
    name: str
    email: str
    address: str

    def __init__(self, id: uuid.UUID, name: str, email: str, address: str):
        self.id = str(id)
        self.name = name
        self.email = email
        self.address = address


class ReceptionOutputModel:
    id: str
    order_id: str
    user: Optional[UserOutputModel]
    reception_date: str

    def __init__(self, id: uuid.UUID, order_id: uuid.UUID, user: Optional[UserOutputModel], reception_date: datetime):
        self.id = str(id)
        self.order_id = str(order_id)
        self.user = user
        self.reception_date = reception_date.isoformat()


class OrderOutputModel:
    id: str
    pyme: PymeOutputModel
    distribution_center: DistributionCenterOutputModel
    dispatch_date: str
    status: int
    total_weight: float
    total_volume: float
    preparation_status: int
    distribution_status: int
    products: List[ProductOutputModel]
    block: Optional[BlockOutputModel] = None
    incidences: Optional[List[IncidenceOutputModel]] = None
    receptions: Optional[List[ReceptionOutputModel]] = None

    def __init__(
        self,
        id: uuid.UUID,
        pyme: PymeOutputModel,
        distribution_center: DistributionCenterOutputModel,
        dispatch_date: datetime,
        status: OrderStatus,
        total_weight: float,
        total_volume: float,
        preparation_status: int,
        distribution_status: int,
        products: List[ProductOutputModel],
        block: Optional[BlockOutputModel] = None,
        incidences: Optional[List[IncidenceOutputModel]] = None,
        receptions: Optional[List[ReceptionOutputModel]] = None
    ):
        self.id = str(id)
        self.pyme = pyme
        self.distribution_center = distribution_center
        self.dispatch_date = dispatch_date.isoformat()
        self.status = status.value
        self.total_weight = total_weight
        self.total_volume = total_volume
        self.preparation_status = preparation_status
        self.distribution_status = distribution_status
        self.products = products
        self.block = block
        self.incidences = incidences or []
        self.receptions = receptions or []

    @property
    def status_name(self) -> str:
        return OrderStatus(self.status).name
