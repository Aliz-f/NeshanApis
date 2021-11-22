from django.db.models import fields
from .models import Address
from rest_framework import serializers

class AddressSerializers(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'

class LatLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['latitude', 'longtitude']