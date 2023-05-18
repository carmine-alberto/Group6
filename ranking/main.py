import datetime

import requests
import time

#Local imports
from ranking.localdata import master_satellites
from ranking.ranking import rank_satellites
from ranking.timeliness import calculate_travel_time_and_orbit_duration

MINIMUM_TIME_BETWEEN_EVENTS = 300

rankings = []
def get_rankings():
    return rankings


while True:
    #TODO Update with actual API


    group5_url = "https://group5/api/"  # temporarly
    response_location_data = requests.get(group5_url)
    target_location = response_location_data.json()

    # if reply is valid
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



    for index, subarea in enumerate(subareas):

        # TODO Data taken from Group 5
        event_id = 123
        aoi_id = 34

        timestamp = datetime.datetime(2023, 2, 6, 8, 0, 0) #6 Feb 23

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

        '''
        Not using this snippet right now - left for future improvements
        
        # url = "https://api.n2yo.com/rest/v1/satellite/above/41.702/-76.014/0/70/18/&apiKey=RFLDHD-2N265V-UFLW6Z-512K"
        start_url = "https://api.n2yo.com/rest/v1/satellite/above/"
        # TODO Check other parameters now hardcoded like altitude (0)
        api_key = "/0/70/18/&apiKey=RFLDHD-2N265V-UFLW6Z-512K"
    
        # Call n2yo to check what satellites are close to the received area
        n2yo_endpoint = start_url + target_location["lat"] + '/' + target_location["lon"] + api_key
        above_data = requests.get(n2yo_endpoint)
        '''

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
            (satellite["travelTime"], satellite_data["orbitDuration"]) = \
                calculate_travel_time_and_orbit_duration(satellite, target_location, timestamp)


        subarea_ranking = rank_satellites(subarea, weather_details, event_type, satellites)

        rankings.append(
            {
                "id": [event_id, aoi_id],
                "ranking": subarea_ranking
            }
        )

        time.sleep(MINIMUM_TIME_BETWEEN_EVENTS)

    # TODO if reply is invalid, ask again





