from django.shortcuts import render

from django.http import HttpResponse
import json


from django.views.decorators.csrf import csrf_exempt

#Local imports
from ranking.utils import parse_body
from ranking.utils import validate_date
from ranking.main import create_subareas_ranking

event_aoi_rankings = []
@csrf_exempt
def index(request):
    if request.method == "GET":
        return HttpResponse(
            '<body>            <form            method = "post"            action = "http://127.0.0.1:8000/ranking/" >            <input            type = "text"            name = "input1" >            <input            type = "text"            name = "input2" >            <input            type = "submit"            value = "Submit" >        </form>        </body>')
    if request.method == "POST":
        subareas = parse_body() #WEATHER DATA + EVENT + AOI + LOCATION TODO parse the real request body
        sxh = subareas[0]["sxh"]
        event_id = sxh["EventID"]['0'] #TODO should be sxk-independent
        aoi_id = subareas[0]["sxh"]["AOI_ID"]['0']

        #Input checks on query parameters #TODO Reenable them, in the GET request possibly
        '''
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
        '''
        output_ranking = []
        ranking_exists = False
        for ranking in event_aoi_rankings:
            if ranking["event_id"] == event_id and ranking["aoi_id"] == aoi_id:
                ranking_exists = True
                output_ranking = ranking
                break


        if not ranking_exists:
            subareas_ranking = create_subareas_ranking(subareas)
            output_ranking = {
                "ranking_ord": "desc",
                'event_id': event_id,
                'aoi_id': aoi_id,
                'subareas': subareas_ranking
            }

            event_aoi_rankings.append(output_ranking) #TODO clone somewhere, here or in the return statement

        reply = {}
        reply['ranking'] = output_ranking

        #TODO Return JSON, not HTTP
        return HttpResponse(json.dumps(reply))




