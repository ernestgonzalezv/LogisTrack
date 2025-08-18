from typing import List, Optional
from datetime import datetime
import uuid

from apps.order_processes.application.features.orders.models.output.orders_output_model import PymeOutputModel, \
    DistributionCenterOutputModel, DriverOutputModel, ProductOutputModel, BlockOutputModel, IncidenceOutputModel, \
    OrderOutputModel
from apps.order_processes.domain.entities.order import Order
from apps.order_processes.domain.entities.block import Block
from apps.order_processes.domain.entities.incidence import Incidence
from apps.order_processes.domain.entities.order_product import OrderProduct
from apps.order_processes.domain.entities.driver import Driver
from apps.order_processes.domain.entities.distribution_center import DistributionCenter
from apps.order_processes.domain.entities.pyme import Pyme


class BlockMapper:

    @staticmethod
    def map_pyme(pyme: Pyme) -> PymeOutputModel:
        return PymeOutputModel(id=pyme.id, name=pyme.name, city=pyme.city)

    @staticmethod
    def map_distribution_center(dc: DistributionCenter) -> DistributionCenterOutputModel:
        return DistributionCenterOutputModel(id=dc.id, name=dc.name, city=dc.city)

    @staticmethod
    def map_driver(driver: Optional[Driver]) -> Optional[DriverOutputModel]:
        if driver is None:
            return None
        return DriverOutputModel(id=driver.id, name=driver.name, phone=driver.phone, email=driver.email)

    @staticmethod
    def map_products(products: List[OrderProduct]) -> List[ProductOutputModel]:
        output: List[ProductOutputModel] = []
        for op in products:
            output.append(
                ProductOutputModel(
                    id=op.product.id,
                    sku=op.product.sku,
                    name=op.product.name,
                    description=op.product.description,
                    quantity=op.quantity
                )
            )
        return output

    @staticmethod
    def map_block(block: Optional[Block]) -> Optional[BlockOutputModel]:
        if block is None:
            return None
        return BlockOutputModel(
            id=block.id,
            creation_date=block.creation_date,
            driver=BlockMapper.map_driver(block.driver)
        )

    @staticmethod
    def map_incidences(incidences: Optional[List[Incidence]]) -> List[IncidenceOutputModel]:
        if not incidences:
            return []
        return [
            IncidenceOutputModel(
                id=i.id,
                type=i.type,
                description=i.description,
                date=i.date,
                status=i.status
            ) for i in incidences
        ]

    @staticmethod
    def map_order(order: Order) -> OrderOutputModel:
        return OrderOutputModel(
            id=order.id,
            pyme=BlockMapper.map_pyme(order.pyme),
            distribution_center=BlockMapper.map_distribution_center(order.distribution_center),
            dispatch_date=order.dispatch_date,
            status=order.status,
            total_weight=order.total_weight,
            total_volume=order.total_volume,
            products=BlockMapper.map_products(order.products),
            block=BlockMapper.map_block(order.block),
            incidences=BlockMapper.map_incidences(order.incidences)
        )

