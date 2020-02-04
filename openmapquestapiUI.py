#Sheila Truong 53588737
# Project 3

import Build_Mapquest
import Mapquest_classes


def get_number():
    '''user inputs a number of how many locations they want'''
    user = int(input())

    return user
        
def get_address():
    '''user inputs the same amount of address to the number they first
    inputted'''
    result = []
    number = get_number()
    for item in range(number):
        address = input()
        result.append(address)
        
    return result
        

def get_options():
    '''user inputs the same amount of options to the number they first
    inputted'''
    result = []
    number = get_number()
    for item in range(number):
        options = input()
        result.append(options)
        
    return result


##def json_version():
##    '''saves the url into a variable from the build_search_url function'''
##
##    address = get_address()
##
##
##    final_url = Build_Mapquest.build_search_url(address)
##
##    
##    json_result = Build_Mapquest.get_result(final_url)
##
##    return json_result


def get_url():
    '''saves the url into a variable from the build_search_url function'''
    address = get_address()
    
    final_url = Build_Mapquest.build_search_url(address)

    return final_url

def get_json_result(url : str):
    '''uses the url to make the json result from the get_url function'''

    json_result = Build_Mapquest.get_result(url)

    return json_result

def get_elevation():
    '''user inputs the location they want and this returns the elevation
    for that one location'''
    
    search_url = get_url()
    json_result = get_json_result(search_url)
 
    result = []
    for item in json_result['route']['locations']:
        lat = item['latLng']['lat']
        lng = item['latLng']['lng']
        result.append((lat,lng))

    description = []
    for coordinates in result:
        
        final_url = Build_Mapquest.build_elevation_url(url)

        json = get_json_result(final_url)
        
        description.append(json)
                
    return description        
            
        
        
        
        
def handle_inputs():
    '''performs the right output for each options from get_options'''
    try:
        result = []
        address = get_address()
        outputs = get_options()
        search_url = get_url()
        json_result = get_json_result(search_url)
        

        for element in outputs:
            if element == 'STEPS':
                steps = Mapquest_classes.Steps(json_result)
                result.append(steps)
            elif element == 'TOTALDISTANCE':
                distance = Mapquest_classes.Distance(json_result)
                result.append(distance)
            elif element == 'TOTALTIME':
                time = Mapquest_classes.Time(json_result)
                result.append(time)
            elif element == 'LATLONG':
                coordinates = Mapquest_classes.LatLng(json_result)
                result.append(coordinates)
            elif element == 'ELEVATION':
                json_format_elevation = get_elevation()
                elevation = Mapquest_classes.Elevation(json_format_elevation)
                result.append(elevation)
                
                
        return_calc = Mapquest_classes.run_calcs(result)
    
        print()
        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
    except:
        print()
        print('MAPQUEST ERROR')







if __name__ == '__main__':
    handle_inputs()
