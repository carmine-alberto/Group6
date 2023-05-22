from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
import requests
import json


#Local imports
from ranking.localdata import master_satellites
from ranking.ranking import rank_satellites
from ranking.timeliness import calculate_travel_time_and_orbit_duration
from ranking.main import get_rankings

rankings = []

def index(request):
    event_id = request.GET.get('event_id')
    aoi_id = request.GET.get('aoi_id')
    rankings = get_rankings()

    #TODO sanitize input

    reply = {}
    for ranking in rankings:
        if ranking["id"]["event_id"] == event_id and ranking["id"]["aoi_id"] == aoi_id:
            reply['ranking'].insert(index, {
                'ranking_ord': "asc",
                'event_id': event_id,
                'aoi_id': aoi_id,
                # Retrieved from Group 5 API call
                'sub_area_centroid': [subarea['centroid']['x'], subarea['centroid']['y']],
                'geometry': subarea["geometry"],
                'satlist': subarea_ranking
            })

    if reply == {}:
        reply['ranking'] = "The provided ID tuple doesn't match any ranking in our database"

    #TODO Return JSON, not HTTP
    return HttpResponse(json.dumps(reply))



        



