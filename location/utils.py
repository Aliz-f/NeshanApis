import requests
from requests import api

def get_address(lat, long):
    try:
        url = 'https://api.neshan.org/v2/reverse?lat={}&lng={}'.format(lat, long)
        headres = {'Api-Key': 'service.s1pJdGf1UVGsXCaBYK9VzyONnRngx4JYW86OTcs3'}
        res = requests.get(url, headers=headres)
        return res.json()
    except requests.exceptions.HTTPError as error:
        print(error) 
 