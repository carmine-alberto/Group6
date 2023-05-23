import datetime
import pandas
import requests
import geohash



#Local imports
from ranking.localdata import master_satellites
from ranking.ranking import rank_satellites
from ranking.timeliness import calculate_travel_time_and_orbit_duration
from ranking.localdata import external_API_enabled
from utils import parse_body

TESTING_FACTOR = 1
MINIMUM_TIME_BETWEEN_EVENTS = 300 * TESTING_FACTOR
MINIMUM_TIME_AFTER_FAILURE = 60 * TESTING_FACTOR


rankings = []

def create_ranking(subarea_parameters, weather_details, event_type, satellites):

        subareas = parse_body()

        subareas_keys = list(subareas[0].keys())

        if subareas != "error":
            for index, subarea_key in enumerate(subareas_keys): #if enumerate doesnt work on keys, go list(keys)

                subarea_parameters = pandas.DataFrame(subareas(subarea_key))

                event_id = subarea_parameters["EventID"][0]
                aoi_id = subarea_parameters["AOI_ID"][0]
                lat, lon = geohash.decode(subarea_key)
                alt = 0
                #TODO understand what happens with this one geometry = subarea_parameters["features"][0]["geometry"]

                date_format = "%Y-%m-%dT%H:%M:%S"
                timestamp = datetime.datetime.strptime(subarea_parameters["features"][0]["properties"]["time"],
                                                       date_format)  # 6 Feb 23 - Comment when out of demo

                weather_details = {
                    "visibility": 1 - float(subarea_parameters["features"][0]["properties"]["cloudcover"]) / 100,
                    "isDay": True if subarea_parameters["features"][0]["properties"]["day/night"] == 0 else False
                    # 0 for day
                }

                event_type = "EARTHQUAKE"  # TODO MISSING: ask them

                satellites = master_satellites

                n2yo_url = "https://api.n2yo.com/rest/v1/satellite/tle/"
                api_key = "apiKey=RFLDHD-2N265V-UFLW6Z-512K"

                # Call n2yo to check what satellites are close to the received area

                '''
                # Call to NASA API to get satellite TLE data
                Removed, now using N2YO
                tle_url = "https://tle.ivanstanojevic.me/api/tle/"
                '''
                for satellite in satellites:
                    sat_id = satellite["id"]
                    n2yo_endpoint = n2yo_url + sat_id + "?" + api_key

                    if external_API_enabled:
                        satellite_data_request = requests.get(n2yo_endpoint)
                        satellite_data = satellite_data_request.json()

                        tle = satellite_data["tle"].split(sep="\r\n")
                        satellite["line1"] = tle[0]
                        satellite["line2"] = tle[1] #TODO make sure this the lines are extracted properly

                    # Attach estimatedTravelTime to each satellite

                    satellite["travelTime"] = calculate_travel_time_and_orbit_duration(satellite, target_location, timestamp)

                subarea_ranking = rank_satellites(subarea_parameters, weather_details, event_type, satellites)

                rankings.append({
                    "id": {"event_id": event_id, "aoi_id": aoi_id},
                    "centroid": centroid,
                    "geometry": geometry,
                    "ranking": subarea_ranking
                })

                print(rankings)
        else:
            print("Empty reply: no events")








