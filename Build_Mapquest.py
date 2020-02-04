# Sheila Truong 53588737
# Project 3

import urllib.parse
import urllib.request
import json
import Mapquest_classes

MAPQUEST_API_KEY = '2OLu86SFciXKOLUJek4uA7RbzRpW7M3k'
BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2'
BASE_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1'
ELEVATION_URL = '&shapeFormat=raw&'

def build_search_url (address: list) -> str:
    '''put together the url for mapquest including the api key and
    special characters'''

    parameters = [
        ('key', MAPQUEST_API_KEY),('from', address[0])
    ]
    
    result = []
    
    for item in address[1:]:
        result.append(item)

    for element in result:
        location = ('to', element)
        parameters.append(location)

    
    encoded_parameters = urllib.parse.urlencode(parameters)

    built_url = BASE_MAPQUEST_URL + '/route?' + encoded_parameters

    return built_url


    

def build_elevation_url(coordinates: str) ->str:
    '''put together the url for the elevation including the api key and
    special characters'''

    
    parameters = [
        ('key', MAPQUEST_API_KEY), ('shapeFormat', 'raw')
    ]

    
    encoded_parameters = urllib.parse.urlencode(parameters)

    built_url = BASE_ELEVATION_URL + '/profile?' + encoded_parameters + '&latLngCollection=' + str(coordinates[0]) + ','+ str(coordinates[1])
        
    return built_url


def get_result(url: str) -> 'Mapquest search result':
    ''' takes in a url and display the whole JSON version of the code'''
    
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_string = response.read().decode(encoding = 'utf-8')
        return json.loads(json_string)
    finally:
        if response != None:
            response.close()


