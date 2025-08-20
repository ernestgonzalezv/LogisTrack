from rest_framework import serializers
from apps.order_processes.presentation.serializers.paging.page_search_args_serializer import PageSearchArgsInputSerializer


class PymeOutputModelSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    city = serializers.CharField()


class DistributionCenterOutputModelSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    city = serializers.CharField()


class ProductOutputModelSerializer(serializers.Serializer):
    id = serializers.CharField()
    sku = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    quantity = serializers.IntegerField()


class DriverOutputModelSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.CharField()


class BlockOutputModelSerializer(serializers.Serializer):
    id = serializers.CharField()
    creation_date = serializers.DateTimeField()
    driver = DriverOutputModelSerializer(required=False, allow_null=True)

    class Meta:
        ref_name = "BlockOutputModelSerializerStage"


class IncidenceOutputModelSerializer(serializers.Serializer):
    id = serializers.CharField()
    type = serializers.IntegerField()
    description = serializers.CharField()
    date = serializers.DateTimeField()
    status = serializers.IntegerField()


class UserOutputModelSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    email = serializers.CharField()
    address = serializers.CharField()


class ReceptionOutputModelSerializer(serializers.Serializer):
    id = serializers.CharField()
    order_id = serializers.CharField()
    user = UserOutputModelSerializer(required=False, allow_null=True)
    reception_date = serializers.DateTimeField()


class OrderOutputModelSerializer(serializers.Serializer):
    id = serializers.CharField()
    pyme = PymeOutputModelSerializer()
    distribution_center = DistributionCenterOutputModelSerializer()
    dispatch_date = serializers.DateTimeField()
    status = serializers.IntegerField()
    total_weight = serializers.FloatField()
    total_volume = serializers.FloatField()
    preparation_status = serializers.IntegerField()
    distribution_status = serializers.IntegerField()
    products = ProductOutputModelSerializer(many=True)
    block = BlockOutputModelSerializer(required=False, allow_null=True)
    incidences = IncidenceOutputModelSerializer(many=True, required=False)
    receptions = ReceptionOutputModelSerializer(many=True, required=False)


class PagedOrdersResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    message = serializers.CharField(allow_blank=True)
    data = OrderOutputModelSerializer(many=True)
    page_index = serializers.IntegerField()
    page_size = serializers.IntegerField()
    total_count = serializers.IntegerField()
    total_pages = serializers.IntegerField()
    has_previous = serializers.BooleanField()
    has_next = serializers.BooleanField()

    class Meta:
        ref_name = "PagedOrdersResponseSerializerStage"


class GetBlocksInputSerializer(serializers.Serializer):
    page_args = PageSearchArgsInputSerializer()
