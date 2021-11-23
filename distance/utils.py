import requests
from rest_framework.response import Response
from location.utils import get_address

def get_distance(source,destination):
    print(source)
    print(destination)
    sourceLat = source.get('latitude', '')
    sourceLong = source.get('longtitude', '')
    destLat = destination.get('latitude', '')
    destLong = destination.get('longtitude', '')
    source_address = get_address(sourceLat, sourceLong)
    destination_address = get_address(destLat, destLong)
    url = 'https://api.neshan.org/v1/distance-matrix?origins={},{}&destinations={},{}'.format(sourceLat, sourceLong, destLat, destLong)
    headres = {'Api-Key': 'service.s1pJdGf1UVGsXCaBYK9VzyONnRngx4JYW86OTcs3'}
    response = requests.get(url, headers=headres)
    print(Response)
    response = response.json().get('rows')[0].get('elements')[0]
    return response, source_address, destination_address

