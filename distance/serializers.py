from django.db.models import fields
from .models import DistanceLocation
from location.models import Address
from rest_framework import serializers

# class latlongSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DistanceLocation
#         fields = 

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class sourcedestinationSerializer(serializers.ModelSerializer):
    source_address = AddressSerializer()
    destination_address = AddressSerializer()
    
    class Meta:
        model = DistanceLocation
        fields = ['source_address', 'destination_address']

class DistanceSerializer(serializers.ModelSerializer):
    
    source_address = AddressSerializer()
    destination_address = AddressSerializer()
    
    class Meta:
        model = DistanceLocation
        fields = '__all__'

    def create(self, validated_data):
        print('validated data: ',validated_data)
        source = validated_data.pop('source_address')
        destination = validated_data.pop('destination_address')
        print(source)
        print(destination)
        source_addr = Address.objects.create(**source)
        destination_addr = Address.objects.create(**destination)
        # print('***********')
        # print(validated_data)
        distance = validated_data.get('distance_km')
        duration = validated_data.get('duration')
        return DistanceLocation.objects.create(source_address=source_addr, destination_address=destination_addr, distance_km=distance, duration=duration)
