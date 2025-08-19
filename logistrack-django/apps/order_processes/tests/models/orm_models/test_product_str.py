import pytest

from apps.order_processes.infrastructure.orm_models.models import Product


@pytest.mark.django_db
def test_product_str():
    product = Product.objects.create(sku="SKU123", name="Product Test", description="Desc")
    assert str(product) == "Product Test (SKU123)"
