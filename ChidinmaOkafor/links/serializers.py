from rest_framework import serializers
from .models import Links
from rest_framework import serializers

class LinkSerializer(serializers.Serializer):
    class Meta:
        model= Links
        field='__all__'