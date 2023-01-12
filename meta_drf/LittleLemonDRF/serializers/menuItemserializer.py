from rest_framework import serializers

from ..models import MenuItem
class MenuItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='categorey.title')

    class Meta:
        model = MenuItem

        fields = ['title', 'price', 'category_name']