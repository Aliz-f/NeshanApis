from django.db.models import fields
from .models import Distance
from location.models import Address
from rest_framework import serializers

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['latitude', 'longtitude', 'state', 'city', 'address']

class sourcedestinationSerializer(serializers.ModelSerializer):
    source_address = AddressSerializer()
    destination_address = AddressSerializer()
    
    class Meta:
        model = Distance
        fields = ['source_address', 'destination_address']

class DistanceSerializer(serializers.ModelSerializer):
    
    source_address = AddressSerializer()
    destination_address = AddressSerializer()
    
    class Meta:
        model = Distance
        fields = ['source_address', 'destination_address', 'distance_km', 'duration']

    def create(self, validated_data):
        source = validated_data.pop('source_address')
        destination = validated_data.pop('destination_address')
        source_addr = Address.objects.create(**source)
        destination_addr = Address.objects.create(**destination)
        distance = validated_data.get('distance_km')
        duration = validated_data.get('duration')
        return Distance.objects.create(source_address=source_addr, destination_address=destination_addr, distance_km=distance, duration=duration)
