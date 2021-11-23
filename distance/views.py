from rest_framework import generics, status
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Distance
from .serializers import DistanceSerializer, sourcedestinationSerializer
from .utils import get_distance

# Create your views here.
class setDistance(generics.GenericAPIView):
    serializer_class = sourcedestinationSerializer
    queryset = Distance.objects.all()

    def post(self, request):
        data = request.data
        source = data.pop('source_address', '')
        destination = data.pop('destination_address' , '')
        response, source_address, destination_address = get_distance(source, destination)
        if response:
            soure_object = {  'latitude':source.get('latitude'),
                            'longtitude': source.get('longtitude'),
                            'state':source_address.get('state'),
                            'city': source_address.get('city'),
                            'address': source_address.get('formatted_address')}
            
            destination_object = {    'latitude':destination.get('latitude'),
                                    'longtitude': destination.get('longtitude'),
                                    'state':destination_address.get('state'),
                                    'city': destination_address.get('city'),
                                    'address': destination_address.get('formatted_address')} 
            
            data['source_address'] = soure_object
            data['destination_address'] = destination_object
            data['distance_km']  = response.get('distance').get('text')
            data['duration'] = response.get('duration').get('text')
        serializer = DistanceSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            distance = Distance.objects.all()
            serializer = DistanceSerializer(distance, many= True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Distance.DoesNotExist():
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)        
            
