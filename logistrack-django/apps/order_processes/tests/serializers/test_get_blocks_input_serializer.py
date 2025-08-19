import uuid

import pytest
from django.utils import timezone

from apps.order_processes.presentation.serializers.orders.orders_serializer import GetBlocksInputSerializer


@pytest.mark.django_db
def test_get_blocks_input_serializer():
    input_data = {"page_args": {"page_index": 1, "page_size": 5}}
    serializer = GetBlocksInputSerializer(data=input_data)
    assert serializer.is_valid(), serializer.errors
    assert serializer.validated_data["page_args"]["page_index"] == 1
