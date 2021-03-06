from dataclasses import field
from rest_framework import serializers
from .models import Contact


class ContactDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'