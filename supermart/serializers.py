from rest_framework import serializers
from .models import Item

# Serializer for Items
class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name','category','sub_category','amount']
