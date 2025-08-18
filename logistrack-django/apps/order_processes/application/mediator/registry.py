from apps.order_processes.application.features.orders.handler.orders_query_handler import \
    BlockProcessesQueryHandler
from apps.order_processes.application.features.orders.queries.get_orders_query import GetOrdersQuery
from apps.order_processes.application.mediator.mediator import Mediator
from apps.order_processes.infrastructure.repositories.order_repository import OrderRepository

mediator = Mediator()

#repo module
orderRepository = OrderRepository()

#mediator module
mediator.register(GetOrdersQuery, lambda : BlockProcessesQueryHandler(orderRepository))