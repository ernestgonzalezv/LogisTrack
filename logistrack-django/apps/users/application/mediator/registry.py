from apps.users.application.features.block_processes.handler.block_processes_query_handler import \
    BlockProcessesQueryHandler
from apps.users.application.features.block_processes.queries.get_blocks_query import GetOrdersQuery
from apps.users.application.mediator.mediator import Mediator
from apps.users.infrastructure.repositories.order_repository import OrderRepository

mediator = Mediator()

#repo module
orderRepository = OrderRepository()

#mediator module
mediator.register(GetOrdersQuery, lambda : BlockProcessesQueryHandler(orderRepository))