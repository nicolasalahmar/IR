from rest_framework import serializers
from Search.models import SearchRequest


class SearchRequestSerializer(serializers.ModelSerializer):
    dataset = serializers.ChoiceField(choices=SearchRequest.DS_CHOICES)
    search_field = serializers.CharField(max_length=256)

    class Meta:
        model = SearchRequest
        fields = '__all__'
