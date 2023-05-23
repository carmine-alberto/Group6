from django.shortcuts import render

from django.http import HttpResponse
import json
import dateutil

from django.views.decorators.csrf import csrf_exempt

#Local imports
from ranking.utils import parse_body
from ranking.main import create_ranking


rankings = []

def validate_date(date):
    try:
        dateutil.parser.parse(date)
        return True
    except Exception as e:
        return False




@csrf_exempt
def index(request):
    if request.method == "GET":
        if request.method == "GET":
            return HttpResponse(
                '<body>            <form            method = "post"            action = "http://127.0.0.1:8000/ranking/" >            <input            type = "text"            name = "input1" >            <input            type = "text"            name = "input2" >            <input            type = "submit"            value = "Submit" >        </form>        </body>')
    if request.method == "POST":
        subareas = parse_body() #WEATHER DATA + EVENT + AOI + LOCATION
        event_id = subareas[0]["sxk"]["EventID"][0] #TODO should be sxk-independent
        aoi_id = subareas[0]["sxk"]["AOI_ID"][0]

        #TODO sanitize input

        reply = {}

        #Input checks on query parameters
        ''''''
        if int(aoi_id)<1 or int(aoi_id)>999:
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

        ranking_exists = False
        for ranking in rankings:
            if ranking["id"]["event_id"] == event_id and ranking["id"]["aoi_id"] == aoi_id:
                ranking_exists = True
                break

        if not ranking_exists:
            ranking = create_ranking(subareas, weather_details, event_type, satellites)

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




