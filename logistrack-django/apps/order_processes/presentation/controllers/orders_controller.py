from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.order_processes.application.core.paging.helpers import parse_pagination_from_request
from apps.order_processes.application.core.paging.models.paged_response import PagedResponse
from apps.order_processes.application.features.orders.queries.get_orders_query import GetOrdersQuery
from apps.order_processes.application.mediator.registry import mediator
from apps.order_processes.presentation.serializers.orders.orders_serializer import (
    PagedOrdersResponseSerializer, GetBlocksInputSerializer
)

class OrderController(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=["Orders"],
        operation_id="Get Orders",
        request_body=GetBlocksInputSerializer,
        responses={200: openapi.Response('Orders', PagedOrdersResponseSerializer)}
    )
    def post(self, request):
        try:
            page_args = parse_pagination_from_request(request.data)
            result: PagedResponse = mediator.send(GetOrdersQuery(page_args=page_args))
            return Response(PagedOrdersResponseSerializer(result).data)
        except Exception as e:
            error_response = PagedResponse(
                data=[],
                page_index=0,
                page_size=0,
                total_count=0,
                success=False,
                message="There has been an error processing your request"
            )
            return Response(PagedOrdersResponseSerializer(error_response).data)


