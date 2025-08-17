# Serializer para FilterOption
from rest_framework import serializers



class FilterOptionSerializer(serializers.Serializer):
    field = serializers.CharField()
    value = serializers.CharField()

# Serializer para SortingOption
class SortingOptionSerializer(serializers.Serializer):
    field = serializers.CharField()
    direction = serializers.CharField(default="asc")  # solo asc o desc

# Serializer para PageSearchArgsInput
class PageSearchArgsInputSerializer(serializers.Serializer):
    page_index = serializers.IntegerField(default=0)
    page_size = serializers.IntegerField(default=20)
    filtering_options = FilterOptionSerializer(many=True, required=False)
    sorting_options = SortingOptionSerializer(many=True, required=False)

from rest_framework import serializers

class PagedResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    message = serializers.CharField(allow_blank=True, required=False)
    data = serializers.ListField(allow_null=True)
    page_index = serializers.IntegerField()
    page_size = serializers.IntegerField()
    total_count = serializers.IntegerField()
    total_pages = serializers.IntegerField()
    has_previous = serializers.BooleanField()
    has_next = serializers.BooleanField()

    def __init__(self, *args, data_serializer=None, **kwargs):
        """
        data_serializer: Serializer que se usará para cada item de 'data'
        """
        super().__init__(*args, **kwargs)
        if data_serializer:
            # Si se pasa un serializer, usamos ListField con child
            self.fields['data'] = serializers.ListField(
                child=data_serializer(), allow_empty=True
            )

    def to_representation(self, instance):
        """
        Convierte la instancia de PagedResponse a dict compatible con JSON.
        Se asegura de que 'data' sea lista y serializa cada item usando el child serializer si existe.
        """
        ret = super().to_representation(instance)
        data = getattr(instance, 'data', None)

        if data is None:
            ret['data'] = []
        else:
            # Si hay un serializer hijo, usamos su to_representation
            child_serializer = getattr(self.fields['data'], 'child', None)
            if child_serializer:
                ret['data'] = [child_serializer.to_representation(item) for item in data]
            else:
                ret['data'] = list(data) if not isinstance(data, list) else data

        return ret
