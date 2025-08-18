import uuid

import pytest

from apps.order_processes.domain.entities.order_product import OrderProduct
from apps.order_processes.domain.entities.product import Product
from apps.order_processes.presentation.serializers.orders.orders_serializer import ProductOutputModelSerializer


@pytest.mark.django_db
def test_product_serializer():
    product = Product(id=uuid.uuid4(), sku="SKU123", name="Producto Test", description="Desc")
    order_product = OrderProduct(product=product, quantity=5)
    serializer = ProductOutputModelSerializer({
        "id": str(product.id),
        "sku": product.sku,
        "name": product.name,
        "description": product.description,
        "quantity": order_product.quantity
    })
    data = serializer.data
    assert data["name"] == "Producto Test"
    assert data["quantity"] == 5
