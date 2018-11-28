
import requests


def geocoder(address):
    parameters = {'address':address, 'sensor':'false'}
    base = ''
    response = requests.get(base, params=parameters)
    answer = response.json()
    print(answer['results']['0']['geometry']['location'])


