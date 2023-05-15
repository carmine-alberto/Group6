from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
import requests
import json

 #SATELLITES IMPORTS
 #pyorbital.orbital TLE is missing - TODO check how to handle that
from pyorbital import tlefile
from datetime import datetime, timedelta
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

        weather_details = {
            "visibility": 0.3,
            "isDay": True
        }
        #TODO get from group5 data

        event_type = "HURRICANE"
        #TODO same as above

        subarea_ranking = rank_satellite(subarea, weather_details, event_type) #extract details and type from group5 reply
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
## key1: name
## key2: line1
## key3: line2
## key4: minimumSnapshotArea
## key5: orbitDuration
tle_url = "https://tle.ivanstanojevic.me/api/tle/"
sat_id = "43638" #temporarly
tleEndpoint = tle_url + sat_id
satelliteData_request = requests.get(tleEndpoint)
satelliteData = satelliteData_request.json()
# need to be read from a file TODO
minimumSnapshotArea = 1
orbitDuration = 2
 
#targetLocation - API request to group 5 to obtain the event location
## key1: lat
## key2: lon
## key3: alt
##TODO Check Varun is passing the right parameters in his calls
group5_url = "https://group5/api/" #temporarly
response_location_data = requests.get(group5_url)
targetLocation = response_location_data.json()

#apiInfo - API request to group 7 to obtain the information about API provider for each satellite
group7_url = "https://group7/api/" #temporarly

#ENSURES
## The arrival time (UTC) if the satellite is going to cross the target location
## -1 if it's never going to cross the target location
def calculate_travel_time(satelliteData, targetLocation):
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
    now = time;

    dt_per_orbit = orbitDuration / dt
    
    while dt_per_orbit > 0:
        pos, _ = tle.get_position(time)
        dist = pos.distance_from(lat, lon, alt)
        # Here, we should consider the area size too. If it's too large, there could be some pieces missing      
        if dist < sqrt(minimumSnapshotArea): # If satellite is within 5 km of the location, break out of the loop - TODO the threshold is selected by picking the square root of the minimum snapshot area
            return time - now
        time += timedelta(seconds=dt)
        dt_per_orbit -= 1

    #Done like this because of the formula in the rating algorithm: 10(1 - delta/orbitDuration) -> 0 if no match is found
    return orbitDuration


