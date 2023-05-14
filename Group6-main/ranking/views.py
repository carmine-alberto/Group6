from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
import requests
import json

 #SATELLITES IMPORTS
 #pyorbital.orbital TLE is missing - TODO check how to handle that
from pyorbital import tlefile
from datetime import datetime
from math import sqrt


def index(request):
    event_id = request.GET.get('event_id')
    aoi_id = request.GET.get('aoi_id')
    # TODO Populate localData - we could hardcode it, do we really need a DB/file?

    # Hardcoded - will be retrieved from Group 5 API
    subareas = [{'geometry': {
        "type": "Polygon",
        "coordinates": [
               [[100.0, 0.0], [101.0, 0.0], [101.0, 1.0],
                [100.0, 1.0], [100.0, 0.0]]
        ]
    }, 'centroid': {'x': '1', 'y': '2'}}, {'geometry': {
        "type": "Polygon",
        "coordinates": [
                [[100.0, 0.0], [101.0, 0.0], [101.0, 1.0],
                 [100.0, 1.0], [100.0, 0.0]]
        ]
    }, 'centroid': {'x': '2', 'y': '3'}}]

    # url = "https://api.n2yo.com/rest/v1/satellite/above/41.702/-76.014/0/70/18/&apiKey=RFLDHD-2N265V-UFLW6Z-512K"
    start_url = "https://api.n2yo.com/rest/v1/satellite/above/"
    # TODO Check other parameters now hardcoded like altitude (0)
    apiKey = "/0/70/18/&apiKey=RFLDHD-2N265V-UFLW6Z-512K"

    reply = {}
    reply['ranking'] = []
    for index, subarea in enumerate(subareas):

        # TODO Coordinates taken from Group 5
        lat = subarea['centroid']['x']
        long = subarea['centroid']['y']

        # Call n2yo to check what satellites are close to the received area
        n2yoEndpoint = start_url + lat + '/' + long + apiKey

        aboveData = requests.get(n2yoEndpoint)

        subarea_ranking = [
            {"satName": "Landsat",
             "timeliness": 7,
             "suitability_to_weather_type": 3,
             "suitability_to_time_of_the_day": 8,
             "suitability_to_event_type": 5,
             "spatial_resolution": 2,
             "frequency_of_update": 6,
             "cost": 9,
             "data_quality": 4
             },
            {"satName": "Modis",
             "timeliness": 6,
             "suitability_to_weather_type": 3,
             "suitability_to_time_of_the_day": 8,
             "suitability_to_event_type": 5,
             "spatial_resolution": 2,
             "frequency_of_update": 6,
             "price": 9,
             "data_quality": 4
             }
        ]  # TODO ranking_algorithm(subarea, aboveData, localData)
        reply['ranking'].insert(index, {
            'ranking_ord': "asc",
            'event_id': event_id,
            'aoi_id': aoi_id,
            # Retrieved from Group 5 API call
            'sub_area_centroid': [subarea['centroid']['x'], subarea['centroid']['y']],
            'geometry': subarea["geometry"],
            # TODO stored in a "ranking" variable produced by the ranking algorithm, change it
            'satlist': subarea_ranking
        })
        

    return HttpResponse(json.dumps(reply))

#REQUIRES
#satelliteData
tle_url = "https://tle.ivanstanojevic.me/api/tle/"
sat_id = "43638"
tleEndpoint = tle_url + sat_id
satelliteData = requests.get(tleEndpoint)
#print(satelliteData)
print(type(satelliteData))
print(satelliteData.json()["name"])
print(satelliteData.get("name"))
#satelliteData DICTIONARY

## key1: name
## key2: line1
## key3: line2
## key4: minimumSnapshotArea
## key5: orbitDuration
""" 
#targetLocation - API request to group 5 to obtain the event location
group5_url = "https://group5/api/" #temporarly
event_location_data = requests.get()
## key1: lat
## key2: lon
## key3: alt

#apiInfo - API request to group 7 to obtain the information about API provider for each satellite
group7_url = "https://group7/api/" #temporarly

""" 

""" 

def predictionAlgorithm(satelliteData, targetLocation):
    # Specify the TLE data for the satellite 
    tle_data = (
        satelliteData["name"],
        satelliteData["line1"],
        satelliteData["line2"]
    )        
    tle = Tle(*tle_data) #TODO FIX

    # Specify the desired location
    lat = targetLocation["lat"] # New York City latitude
    lon = targetLocation["lon"] # New York City longitude
    alt = targetLocation["alt"] # Altitude in km

    # Calculate the time required for the satellite to reach the specified location
    dt = 300 # Time interval in seconds - TODO What is the LSB we want to use?
    time = datetime.utcnow()

    dt_per_orbit = orbitDuration / dt
    
    while dt_per_orbit
        pos, _ = tle.get_position(time)
        dist = pos.distance_from(lat, lon, alt)
        # Here, we should consider the area size too. If it's too large, there could be some pieces missing      
        if dist < sqrt(minimumSnapshotArea): # If satellite is within 5 km of the location, break out of the loop - TODO the threshold is selected by picking the square root of the minimum snapshot area
            break
        time += timedelta(seconds=dt)

        """
