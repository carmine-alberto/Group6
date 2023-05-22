from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
import requests
import json
import dateutil

#Local imports
from ranking.localdata import master_satellites
from ranking.ranking import rank_satellites
from ranking.timeliness import calculate_travel_time_and_orbit_duration
from ranking.main import get_rankings

rankings = []


def validate_date(date):
    try:
        dateutil.parser.parse(date)
        return True
    except Exception as e:
        return False


def index(request):
    event_id = request.GET.get('event_id')
    aoi_id = request.GET.get('aoi_id')

    reply = {}
    #Input checks on query parameters
    ''''''
    if aoi_id<1 or aoi_id>999:
        reply['ranking'] = "The provided ID tuple doesn't have the correct format: the aoi has not a correct id"

    event_id_sep=event_id.split(sep='-')
    if event_id_sep[0]!="gr1" and event_id_sep[0]!="gr2":
        reply['ranking'] = "The provided ID tuple doesn't have the correct format: the group is wrong"
    elif event_id_sep[1].isalpha()==False:
        reply['ranking'] = "The provided ID tuple doesn't have the correct format: the country is wrong"
    elif validate_date(event_id_sep[2])==False or validate_date(event_id_sep[3])==False:
        reply['ranking'] = "The provided ID tuple doesn't have the correct format: the date-time is wrong"
    elif event_id_sep[4].isalpha()==False: 
        reply['ranking'] = "The provided ID tuple doesn't have the correct format: the event type is wrong"
    
    

    rankings = get_rankings()

    #TODO sanitize input

    
    for ranking in rankings:
        if ranking["id"]["event_id"] == event_id and ranking["id"]["aoi_id"] == aoi_id:
            reply['ranking'] = ranking["ranking"]

    if reply == {}:
        reply['ranking'] = "The provided ID tuple doesn't match any ranking in our database"

    #TODO Return JSON, not HTTP
    return HttpResponse(json.dumps(reply))




