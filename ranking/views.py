from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
import requests
import json

#Local imports
from ranking.localdata import master_satellites
from ranking.ranking import rank_satellites
from ranking.timeliness import calculate_travel_time


def index(request):
    event_id = request.GET.get('event_id')
    aoi_id = request.GET.get('aoi_id')
    # TODO We are currently using these IDs to fill in the objects.
    # They should be used to select the ranking among the stored ones instead.
    # The IDs to put inside the objects are retrieved from group 5 API call


    '''
    TODO Update with actual API
    group5_url = "https://group5/api/"  # temporarly
    response_location_data = requests.get(group5_url)
    target_location = response_location_data.json()
    '''

    # apiInfo - API request to group 7 to obtain the information about API provider for each satellite
    # In theory, since it's static data, we will read a file/hardcode it
    # group7_url = "https://group7/api/"  # temporarly

    # Hardcoded - will be retrieved from Group 5 API
    subareas = [
        {'geometry': {
            "type": "Polygon",
            "coordinates": [
                   [[100.0, 0.0], [101.0, 0.0], [101.0, 1.0],
                    [100.0, 1.0], [100.0, 0.0]]
                ]
            },
        'centroid': {'x': '38.6220905', 'y': '24.5173068', 'z': '5'}
        },
        {'geometry': {
            "type": "Polygon",
            "coordinates": [
                    [[100.0, 0.0], [101.0, 0.0], [101.0, 1.0],
                     [100.0, 1.0], [100.0, 0.0]]
                ]
            },
        'centroid': {'x': '38.527611', 'y': '34.2072482', 'z': '6'}
        }
    ]

    reply = {}
    reply['ranking'] = []
    for index, subarea in enumerate(subareas):

        # TODO Data taken from Group 5
        weather_details = {
            "visibility": 0.3,
            "isDay": True
        }
        event_type = "EARTHQUAKE"
        target_location = {
            "lat": subarea['centroid']['x'],
            "lon": subarea['centroid']['y'],
            "alt": subarea['centroid']['z']
        }


        satellites = master_satellites

        # url = "https://api.n2yo.com/rest/v1/satellite/above/41.702/-76.014/0/70/18/&apiKey=RFLDHD-2N265V-UFLW6Z-512K"
        start_url = "https://api.n2yo.com/rest/v1/satellite/above/"
        # TODO Check other parameters now hardcoded like altitude (0)
        api_key = "/0/70/18/&apiKey=RFLDHD-2N265V-UFLW6Z-512K"

        # Call n2yo to check what satellites are close to the received area
        n2yo_endpoint = start_url + target_location["lat"] + '/' + target_location["lon"] + api_key
        above_data = requests.get(n2yo_endpoint)
        #TODO See IMPROVEMENTS in GDoc

        # Call to NASA API to get satellite TLE data
        tle_url = "https://tle.ivanstanojevic.me/api/tle/"
        for satellite in satellites:
            sat_id = satellite["id"]
            tle_endpoint = tle_url + sat_id
            satellite_data_request = requests.get(tle_endpoint)
            satellite_data = satellite_data_request.json()

            satellite["line1"] = satellite_data["line1"]
            satellite["line2"] = satellite_data["line2"]

            #Attach estimatedTravelTime to each satellite
            satellite["travelTime"] = calculate_travel_time(satellite, target_location)


        subarea_ranking = rank_satellites(subarea, weather_details, event_type, satellites)

        reply['ranking'].insert(index, {
            'ranking_ord': "asc",
            'event_id': event_id,
            'aoi_id': aoi_id,
            # Retrieved from Group 5 API call
            'sub_area_centroid': [subarea['centroid']['x'], subarea['centroid']['y']],
            'geometry': subarea["geometry"],
            'satlist': subarea_ranking
        })
        

    return HttpResponse(json.dumps(reply))


