from django.shortcuts import render

from django.http import HttpResponse
import json


#Local imports
from ranking.utils import parse_body
from ranking.main import create_ranking


rankings = []

def index(request):
    if request.method == "POST":
        body = parse_body() #WEATHER DATA + EVENT + AOI + LOCATION
        event_id = body['event_id']
        aoi_id = body['aoi_id']

        weather_data = 0 #PARSE


        #TODO sanitize input

        reply = {}
        ranking_exists = False
        for ranking in rankings:
            if ranking["id"]["event_id"] == event_id and ranking["id"]["aoi_id"] == aoi_id:
                ranking_exists = True
                break

        if not ranking_exists:
            ranking = create_ranking(subarea, weather_details, event_type, satellites)

            reply['ranking'] = {
                "ranking_ord": "desc",
                'event_id': event_id,
                'aoi_id': aoi_id,
                'sub_area_centroid': [ranking["centroid"]["coordinates"][0], ranking["centroid"]["coordinates"][1], "0"],
                'geometry': ranking["geometry"],
                'satList': ranking["ranking"]
            }

        #TODO Return JSON, not HTTP
        return HttpResponse(json.dumps(reply))




