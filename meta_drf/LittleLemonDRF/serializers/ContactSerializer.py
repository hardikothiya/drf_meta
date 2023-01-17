from rest_framework import serializers

from ..models.contact import ContactDetails


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetails
        fields = ['user', 'number', 'last_name']

        depth = 2
