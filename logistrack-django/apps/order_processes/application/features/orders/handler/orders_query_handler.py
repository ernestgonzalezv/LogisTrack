from typing import List
from apps.order_processes.application.core.paging.map_profiles.page_search_args_profile import PageSearchArgsMapper
from apps.order_processes.application.core.paging.map_profiles.paged_response_mapper import PagedResponseMapper
from apps.order_processes.application.core.paging.models.paged_response import PagedResponse
from apps.order_processes.application.features.orders.map_profiles.orders_mapper import BlockMapper
from apps.order_processes.application.features.orders.queries.get_orders_query import GetOrdersQuery
from apps.order_processes.application.features.orders.validations.get_orders_query_validator import \
    validate_get_blocks_query


class BlockProcessesQueryHandler:
    def __init__(self, repository):
        self.repository = repository

    def handle(self, query: GetOrdersQuery) -> PagedResponse:
        """
        Ejecuta la query para obtener bloques por etapa (stage) y devuelve un PagedResponse
        con la data mapeada a BlocksStageOutputModel.
        """
        try:
            # Validación de input
            validate_get_blocks_query(query)

            # Convertir argumentos de paginación de input a dominio
            page_args = PageSearchArgsMapper.input_to_domain(query.page_args)

            # Obtener data paginada del repositorio
            query_result = self.repository.get_orders_by_stage(page_args)

            pagedResponse = PagedResponseMapper.from_query_result(query_result,
                                                                  lambda order: BlockMapper.map_order(order))

            return pagedResponse

        except Exception as e:
            # En caso de error, devolver PagedResponse vacío con mensaje
            return PagedResponse(
                data=[],
                page_index=0,
                page_size=0,
                total_count=0,
                success=False,
                message="There has been an error processing your request",
            )
