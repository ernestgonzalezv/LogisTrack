from typing import List, Optional

from apps.users.domain.enums.incidence_status import IncidenceStatus
from apps.users.domain.enums.incidence_type import IncidenceType
from apps.users.infrastructure.orm_models.models import Order as InfraOrder, BlockOrder
from apps.users.domain.entities.order import (
    Order, OrderStatus
)
from apps.users.domain.entities.block import Block
from apps.users.domain.entities.incidence import Incidence
from apps.users.domain.entities.order_product import OrderProduct
from apps.users.domain.entities.product import Product
from apps.users.domain.entities.driver import Driver
from apps.users.domain.entities.distribution_center import DistributionCenter
from apps.users.domain.entities.pyme import Pyme


def map_order(o: InfraOrder) -> Order:
    # 🔹 Pyme y Distribution Center
    pyme = Pyme(id=o.pyme.id, name=o.pyme.name, city=o.pyme.city)
    dc = DistributionCenter(id=o.distribution_center.id, name=o.distribution_center.name, city=o.distribution_center.city)

    # 🔹 Bloque y driver
    block_model: Optional[BlockOrder] = None
    driver: Optional[Driver] = None
    if o.blockorder_set.exists():
        block_model = o.blockorder_set.first().block
        if block_model.driver:
            d = block_model.driver
            driver = Driver(id=d.id, name=d.name, phone=d.phone, email=d.email)
    block = Block(id=block_model.id, creation_date=block_model.creation_date, driver=driver) if block_model else None

    # 🔹 Productos
    products: List[OrderProduct] = [
        OrderProduct(
            product=Product(
                id=op.product.id,
                sku=op.product.sku,
                name=op.product.name,
                description=op.product.description
            ),
            quantity=op.quantity
        ) for op in o.orderproduct_set.all()
    ]

    # 🔹 Incidencias
    incidences: List[Incidence] = [
        Incidence(
            id=i.id,
            type=IncidenceType(i.type),
            description=i.description,
            date=i.date,
            status=IncidenceStatus(i.status)
        ) for i in o.incidence_set.all()
    ]

    return Order(
        id=o.id,
        pyme=pyme,
        distribution_center=dc,
        dispatch_date=o.dispatch_date,
        status=OrderStatus(o.status),
        total_weight=o.total_weight,
        total_volume=o.total_volume,
        products=products,
        block=block,
        incidences=incidences
    )

def map_orders(queryset) -> List[Order]:
    return [map_order(o) for o in queryset]
