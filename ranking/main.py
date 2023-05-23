import datetime
import pandas
import requests
import geohash
import copy


#Local imports
from ranking.localdata import master_satellites
from ranking.ranking import rank_satellites
from ranking.timeliness import calculate_travel_time_and_weather_details
from ranking.localdata import external_API_enabled
from ranking.utils import parse_body, get_timestamp

TESTING_FACTOR = 1
MINIMUM_TIME_BETWEEN_EVENTS = 300 * TESTING_FACTOR
MINIMUM_TIME_AFTER_FAILURE = 60 * TESTING_FACTOR




def create_subareas_ranking(subareas):
        rankings = []
        #TODO handle concatenated version
        subareas_keys = list(subareas[0].keys())

        if subareas != "error":
            for index, subarea_key in enumerate(subareas_keys): #if enumerate doesn't work on keys, go list(keys)

                subarea_parameters = pandas.DataFrame(subareas[0][subarea_key])

                lat, lon = geohash.decode(subarea_key)
                alt = 0
                day = "22"#TODO check new format subareas[-1]["day"]
                month = "05" #^subareas[-1]["month"]
                year = "2023" #^subareas[-1]["year"]
                hour = "06"
                minutes = "30"
                seconds = "00"

                event_type = "EARTHQUAKE" #^subareas[-1]["eventType"]

                date_format = "%Y-%m-%dT%H:%M:%S"
                datetime = year + "-" + month + "-" + day + "T" + hour + ":" + minutes + ":" + seconds
                timestamp = get_timestamp(datetime, date_format)  # 6 Feb 23 - Comment when out of demo

                '''
                # Call to NASA API to get satellite TLE data
                Removed, now using N2YO
                tle_url = "https://tle.ivanstanojevic.me/api/tle/"
                '''
                target_location = {
                    "lat": lat,
                    "lon": lon,
                    "alt": alt
                }
                satellites = master_satellites

                n2yo_url = "https://api.n2yo.com/rest/v1/satellite/tle/"
                api_key = "RFLDHD-2N265V-UFLW6Z-512K"
                for satellite in satellites:
                    sat_id = satellite["id"]
                    n2yo_endpoint = n2yo_url + sat_id + "?" + "apiKey=" + api_key

                    if external_API_enabled:
                        # TODO Check for errors or missing satellites - exception? if-else on error code?
                        satellite_data_request = requests.get(n2yo_endpoint)
                        satellite_data = satellite_data_request.json()

                        tle = satellite_data["tle"].split(sep="\r\n")
                        satellite["line1"] = tle[0]
                        satellite["line2"] = tle[1]

                    # Attach estimatedTravelTime to each satellite and obtain weather details in that specific location
                    satellite["travelTime"], satellite["weatherConditions"] = \
                        calculate_travel_time_and_weather_details(satellite, target_location, timestamp, subarea_parameters)

                subarea_ranking = rank_satellites(subarea_parameters, event_type, satellites)

                rankings.append({
                    "centroid": {"lat": lat, "lon": lon, "alt": alt},
                    "ranking": subarea_ranking
                })

            print(rankings)
            return copy.deepcopy(rankings)
        else:
            print("Empty reply: no events")








