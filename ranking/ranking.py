
from ranking.localdata import weights

#ENSURES
#travelTime returned in seconds

def get_travel_time(satellite):
    return float(satellite["travelTime"])


def get_suitability_to_event_rating(satellite, event_type):
    suitability_to_event_rating = 0
    if event_type in [e.name for e in satellite["eventTypes"]]:
        suitability_to_event_rating = 10
    return suitability_to_event_rating

def get_suitability_to_weather_rating(satellite, weather_details):
    visibility_threshold = satellite["visibility_threshold"]
    visibility = weather_details["visibility"]
    delta = visibility - visibility_threshold #TODO threshold should be 0 or close to it for the most powerful, change it
    if delta > 0:
        return 10
    return 10 * (delta + 1)**2

def get_suitability_to_time_of_day_rating(satellite,weather_details):
    time_of_day_rating = 5
    #TODO Actually, some of them work during the night only, so we should have 2 boolean, worksDuringDay too
    if weather_details['isDay'] == True or satellite["worksDuringNight"]==True:
        time_of_day_rating = 10
    elif satellite["worksDuringNight"] == False and weather_details['isDay'] == False:
        time_of_day_rating = 0
    return time_of_day_rating

BEST_RES = 50 #TODO Tweak
WORST_RES = 1000
def get_spatial_resolution_rating(satellite):
    #TODO the rating here should be event-based perhaps - read webpage
    spatial_resolution_rating = 10 * (1 - (satellite['spatialResolution'] - BEST_RES) / (WORST_RES - BEST_RES))
    return spatial_resolution_rating
    
    

        
MAX_FOU = 16 #TODO Extract from satellites list
def get_frequency_of_update_rating(satellite):
    #todo: do the rating logic according to the lookup table
    frequency_of_update_rating = (1 - satellite["frequencyOfUpdate"]/MAX_FOU) * 10
    return frequency_of_update_rating
        
MAX_PRICE = 100 #TODO Extract from sat list
def get_price_rating(satellite):
    #todo: do the rating logic according to the lookup table
    price_rating = (1 - satellite["price"]/MAX_PRICE) * 10
    return price_rating    

def get_data_quality_rating(satellite):
    #todo: do the rating logic according to the lookup table
    data_quality_rating = satellite["dataQualityRating"]
    return data_quality_rating   



def rank_satellites(subarea, weather_details, event_type, satellites):
    filtered_satellites = []
    for satellite in satellites:
        if subarea["centroid"]:
          satellite_travel_time = float(satellite["travelTime"])
          timeliness_rating = 10*(1-satellite_travel_time/float(satellite["orbitDuration"]))
        else: 
            raise Exception("Sorry, no centroid in the input.")


        suitability_to_event_rating= get_suitability_to_event_rating(satellite,event_type)               

        suitability_to_weather_rating= get_suitability_to_weather_rating(satellite,weather_details)   

        suitability_to_time_of_day_rating= get_suitability_to_time_of_day_rating(satellite,weather_details)   

        spatial_resolution_rating= get_spatial_resolution_rating(satellite)

        frequency_of_update_rating= get_frequency_of_update_rating(satellite)

        price_rating = get_price_rating(satellite) 

        data_quality_rating = get_data_quality_rating(satellite)   

        overall_rating = (weights["timeliness"] * timeliness_rating) + (weights["suitability_to_weather_type"] * suitability_to_weather_rating) + (weights["suitability_to_time_of_the_day"] * suitability_to_time_of_day_rating) + (weights["suitability_to_event_type"] * suitability_to_event_rating) + (weights["spatial_resolution"] * spatial_resolution_rating) + (weights["frequency_of_update"] * frequency_of_update_rating) + (weights["price"] * price_rating) + (weights["data_quality"] * data_quality_rating)

        satellite_object_with_all_ratings = {
            "family": satellite["family"],
            "name": satellite["name"],
            "rating": overall_rating,
            "details": {
                "timeliness": timeliness_rating,
                "suitability_to_weather_type": suitability_to_weather_rating,
                "suitability_to_time_of_the_day": suitability_to_time_of_day_rating,
                "suitability_to_event_type": suitability_to_event_rating,
                "geographical_definition": spatial_resolution_rating,
                "frequency_of_update": frequency_of_update_rating,
                "apiURL": satellite["apiName"],
                "price": price_rating,
                "data_quality": data_quality_rating
            }
        }

        filtered_satellites.append(satellite_object_with_all_ratings)

    sorted_satellite_objects = sorted(filtered_satellites, key=lambda x: x['rating'], reverse=True)

    return sorted_satellite_objects
