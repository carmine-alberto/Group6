from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
import requests
import json


def index(request):
    event_id = request.GET.get('event_id')
    aoi_id = request.GET.get('aoi_id')
    # TODO Populate localData - we could hardcode it, do we really need a DB/file?

    # Hardcoded - will be retrieved from Group 5 API
    subareas = [{'geometry': {
        "type": "MultiPolygon",
        "coordinates": [
            [[[102.0, 2.0], [103.0, 2.0], [103.0, 3.0], [102.0, 3.0], [102.0, 2.0]]],
            [[[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]],
             [[100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2]]]
        ]
    }, 'centroid': {'x': '1', 'y': '2'}}, {'geometry':  {
        "type": "MultiPolygon",
        "coordinates": [
            [[[102.0, 2.0], [103.0, 2.0], [103.0, 3.0], [102.0, 3.0], [102.0, 2.0]]],
            [[[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]],
             [[100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2]]]
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
