from django.shortcuts import render
from .serializers import AddressSerializers, LatLongSerializer
from .models import Address
from .utils import get_address
from rest_framework.response import Response
from rest_framework import generics, status
from django.http import HttpResponse, response
# Create your views here.

class NeshanLocation(generics.GenericAPIView):
    serializer_class = LatLongSerializer
    queryset = Address.objects.all()
    
    def post(slef, request):
        data = request.data
        lat = data.get('latitude', '')
        long = data.get('longtitude', '')
        response = get_address(lat, long)
        if response:
            data["city"] = response.get('city', '')
            data["state"] = response.get('state', '')
            data["address"] = response.get('formatted_address', '')
            serializer = AddressSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        try:
            addr = Address.objects.all()
            serializer = AddressSerializers(addr, many= True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Address.DoesNotExist():
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)        
            


    