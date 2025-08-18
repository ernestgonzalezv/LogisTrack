# apps/order_processes/domain/repositories/order_repository.py
from abc import ABC, abstractmethod
from typing import List
from apps.order_processes.application.core.paging.models.page_search_args_input import PageSearchArgsInput
from apps.order_processes.application.core.paging.models.query_result import QueryResult
from apps.order_processes.application.features.orders.models.output.orders_output_model import OrderOutputModel
from apps.order_processes.domain.entities.order import Order


class IOrderRepository(ABC):
    @abstractmethod
    def get_orders_by_stage(
        self,
        page_args: PageSearchArgsInput
    ) -> QueryResult[Order]:
        pass
