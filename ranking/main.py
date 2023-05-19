import datetime

import requests
import time
import threading


#Local imports
from ranking.localdata import master_satellites
from ranking.ranking import rank_satellites
from ranking.timeliness import calculate_travel_time_and_orbit_duration
from ranking.localdata import NASA

TESTING_FACTOR = 1
MINIMUM_TIME_BETWEEN_EVENTS = 300 * TESTING_FACTOR
MINIMUM_TIME_AFTER_FAILURE = 60 * TESTING_FACTOR


rankings = []

def get_rankings():
    return rankings


def polling_function():

    while True:
        # TODO Update with actual API
        group5_url = "https://group5/api/"  # temporarly
        # TODO uncomment when G5 API is ready - response_location_data = requests.get(group5_url)

        # if reply is valid
        # Hardcoded - will be retrieved from Group 5 API
        # subareas = response_location_data.json() #Uncomment when finished
        subareas = [
            {
                "type": "FeatureCollection",
                "features": [
                    {
                        "id": "0",
                        "type": "Feature",
                        "properties": {
                            "time": "2023-02-06T00:00:00",
                            "AOI_ID": "10",
                            "EventID": "10",
                            "temperature": 14.1,
                            "precipitationProbability": 0,
                            "cloudcover": 84,
                            "day/night": 0,
                            "centroid": {
                                "type": "Point",
                                "coordinates": [45.464664, 9.18854]
                            }
                        },
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [
                                [4.377184, 50.854457],
                                [4.477184, 50.854457],
                                [4.477184, 52.854457],
                                [4.377184, 52.854457]
                            ],
                        },
                    }]
            }]

        if subareas != "error":
            for index, subarea in enumerate(subareas):

                event_id = subarea["features"][0]["properties"]["EventID"]
                aoi_id = subarea["features"][0]["properties"]["AOI_ID"]

                date_format = "%Y-%m-%dT%H:%M:%S"
                timestamp = datetime.datetime.strptime(subarea["features"][0]["properties"]["time"],
                                                       date_format)  # 6 Feb 23 - Comment when out of demo

                weather_details = {
                    "visibility": 1 - float(subarea["features"][0]["properties"]["cloudcover"]) / 100,
                    "isDay": True if subarea["features"][0]["properties"]["day/night"] == 0 else False
                    # TODO Ask whether 0 is day or night
                }

                event_type = "EARTHQUAKE"  # TODO MISSING: ask them

                target_location = {
                    "lat": subarea["features"][0]["properties"]["centroid"]["coordinates"][0],
                    "lon": subarea["features"][0]["properties"]["centroid"]["coordinates"][1],
                    "alt": 0  # TODO Not passed as of now, 0
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
                    api_key = "woYxeCG5zRW5m3zxUe4KqLGbRsMzQaoaXLWwgjWX"
                    tle_endpoint = tle_url + sat_id + "?api_key=" + api_key

                    if NASA:
                        satellite_data_request = requests.get(tle_endpoint)
                        satellite_data = satellite_data_request.json()

                        satellite["line1"] = satellite_data["line1"]
                        satellite["line2"] = satellite_data["line2"]

                    # Attach estimatedTravelTime to each satellite

                    satellite["travelTime"], satellite["orbitDuration"] = \
                        calculate_travel_time_and_orbit_duration(satellite, target_location, timestamp)

                subarea_ranking = rank_satellites(subarea, weather_details, event_type, satellites)

                rankings.append({
                    "id": {"event_id": event_id, "aoi_id": aoi_id},
                    "ranking": subarea_ranking
                })

                print(rankings)
                time.sleep(MINIMUM_TIME_BETWEEN_EVENTS)

        else:
            print("Empty reply: no events")
            time.sleep(MINIMUM_TIME_AFTER_FAILURE)








