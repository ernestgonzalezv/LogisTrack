import uuid
from django.db import models

from apps.users.domain.enums.order_status import OrderStatus
from apps.users.domain.enums.incidence_type import IncidenceType
from apps.users.domain.enums.incidence_status import IncidenceStatus


class Pyme(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)

    class Meta:
        db_table = "logistrack_pymes"

    def __str__(self):
        return self.name


class DistributionCenter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)

    class Meta:
        db_table = "logistrack_distributionCenters"

    def __str__(self):
        return self.name


class Driver(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        db_table = "logistrack_drivers"

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = "logistrack_products"

    def __str__(self):
        return f"{self.name} ({self.sku})"


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pyme = models.ForeignKey(Pyme, on_delete=models.CASCADE)
    distribution_center = models.ForeignKey(DistributionCenter, on_delete=models.CASCADE)
    dispatch_date = models.DateTimeField()
    status = models.IntegerField(
        choices=[(status.value, status.name) for status in OrderStatus]
    )
    total_weight = models.FloatField()
    total_volume = models.FloatField()

    class Meta:
        db_table = "logistrack_orders"

    def __str__(self):
        return f"Order {self.id}"


class Block(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "logistrack_blocks"

    def __str__(self):
        return f"Block {self.id}"


class OrderProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = "logistrack_orderProducts"


class BlockOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        db_table = "logistrack_blockOrders"


class Incidence(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    type = models.IntegerField(choices=[(t.value, t.name) for t in IncidenceType])
    description = models.TextField()
    date = models.DateTimeField()
    status = models.IntegerField(
        choices=[(status.value, status.name) for status in IncidenceStatus]
    )

    class Meta:
        db_table = "logistrack_incidences"

    def __str__(self):
        return f"Incidence {self.id} - {self.type}"