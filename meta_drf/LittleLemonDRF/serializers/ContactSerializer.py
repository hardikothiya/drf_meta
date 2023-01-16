from rest_framework import serializers

from ..models.contact import ContactDetails


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetails
        field = ['user', 'number', 'last_name']
