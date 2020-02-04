# Sheila Truong 53588737

import Build_Mapquest
import Mapquest_UI

class LatLng:

    def __init__(self, result):
        self._result = result
        
    def calculate(self):

        print()
        print('LATLONGS')
        
        for location in self._result['route']['locations']:
            lat = '%.2f'%(location['latLng']['lat'])                
            long = '%.2f'%(location['latLng']['lng'])
            if float(lat) > 0 and float(long) > 0:
                print(str(lat)+'N', str(long)+'E')
            elif float(lat) < 0 and float(long) > 0:
                postive = abs(float(lat))
                print(str(positive)+'S', str(long)+'E')
            elif float(lat) > 0 and float(long) < 0:
                positive = abs(float(long))
                print(str(lat)+'N', str(positive)+'W')
            elif float(lat) < 0 and float(long) < 0:
                positive = abs(float(lat))
                postive2 = abs(float(long))
                print(str(postive)+'S', str(positive2)+'W')
 
                
                

            

class Steps:
    def __init__(self, result):
        self._result = result

    def calculate(self):
        print()
        print('DIRECTIONS')
        for item in self._result['route']['legs']:
            for element in item['maneuvers']:
                print(element['narrative'])

class Distance:
    def __init__(self, result):
        self._result = result

    def calculate(self):
        print()
        print('TOTAL DISTANCE: ', round(self._result['route']['distance']), 'miles')

class Time:
    def __init__(self, result):
        self._result = result

    def calculate(self):
        seconds = self._result['route']['time']
        minutes = seconds / 60
        
        print()
        print('TOTAL TIME: ', round(minutes), 'minutes')



class Level:
    def __init__(self, result):
        self._result = result

    def calculate(self):
        print()
        print('ELEVATION')
        
        elev_result = []
        for item in self._result['route']['locations']:
            lat = item['latLng']['lat']
            lng = item['latLng']['lng']
            elev_result.append((lat,lng))
            
        description = []
        for coordinates in elev_result:
            final_url = Build_Mapquest.build_elevation_url(coordinates)
            json_result = Mapquest_UI.get_json_result(final_url)
            description.append(json_result)
    
        for item in description:
            for element in item['elevationProfile']:
                height = round(element['height'] * 3.28)
                print(height)

        
        


def run_calcs(cals:['calc'], json_result: 'Mapquest search result'):
    
    try:
        if json_result['info']['statuscode'] == 400:
            raise KeyError
        
        for calc in cals:
            get_outputs = calc.calculate()

        print()
        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
        return get_outputs

    except KeyError:
        print()
        print('NO ROUTE FOUND')




