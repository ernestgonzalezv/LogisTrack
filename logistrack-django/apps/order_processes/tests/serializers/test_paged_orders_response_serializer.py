import uuid

import pytest
from django.utils import timezone

from apps.order_processes.presentation.serializers.orders.orders_serializer import PagedOrdersResponseSerializer


@pytest.mark.django_db
def test_paged_orders_response_serializer():
    response_data = {
        "success": True,
        "message": "",
        "data": [],
        "page_index": 1,
        "page_size": 10,
        "total_count": 20,
        "total_pages": 2,
        "has_previous": False,
        "has_next": True,
    }
    serializer = PagedOrdersResponseSerializer(response_data)
    data = serializer.data
    assert data["success"] is True
    assert data["total_pages"] == 2