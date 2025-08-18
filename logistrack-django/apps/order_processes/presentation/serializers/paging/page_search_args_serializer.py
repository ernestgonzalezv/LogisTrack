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

