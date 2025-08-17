# apps/users/domain/repositories/order_repository.py
from abc import ABC, abstractmethod
from typing import List
from apps.users.application.core.paging.models.page_search_args_input import PageSearchArgsInput
from apps.users.application.core.paging.models.query_result import QueryResult
from apps.users.application.features.block_processes.models.output.blocks_stage_output_model import OrderOutputModel
from apps.users.domain.entities.order import Order


class IOrderRepository(ABC):
    @abstractmethod
    def get_orders_by_stage(
        self,
        page_args: PageSearchArgsInput
    ) -> QueryResult[Order]:
        pass
