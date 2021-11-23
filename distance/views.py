from django.db.models.lookups import StartsWith
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics, serializers, status
from rest_framework.compat import distinct
from rest_framework.response import Response
from django.http import HttpResponse
from .models import DistanceLocation
from .serializers import AddressSerializer, DistanceSerializer, sourcedestinationSerializer
from .utils import get_distance

# Create your views here.
class setDistance(generics.GenericAPIView):
    serializer_class = sourcedestinationSerializer
    queryset = DistanceLocation.objects.all()

    def post(self, request):
        data = request.data
        source = data.pop('source_address', '')
        destination = data.pop('destination_address' , '')
        response, source_address, destination_address = get_distance(source, destination)
        if response:
            json_soure = {  'latitude':source.get('latitude'),
                            'longtitude': source.get('longtitude'),
                            'state':source_address.get('state'),
                            'city': source_address.get('city'),
                            'address': source_address.get('formatted_address')}
            
            json_destination = {    'latitude':destination.get('latitude'),
                                    'longtitude': destination.get('longtitude'),
                                    'state':destination_address.get('state'),
                                    'city': destination_address.get('city'),
                                    'address': destination_address.get('formatted_address')} 
            
            data['source_address'] = json_soure
            data['destination_address'] = json_destination
            # print(response.get('distance').get('text'))
            # print(response.get('duration').get('text'))
            data['distance_km']  = response.get('distance').get('text')
            data['duration'] = response.get('duration').get('text')
            print('data: ',data)
        serializer = DistanceSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            distance = DistanceLocation.objects.all()
            serializer = DistanceSerializer(distance, many= True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except DistanceLocation.DoesNotExist():
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)        
            
