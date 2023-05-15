import datetime

from localdata import master_satellites

weight_dict = {
    'timeliness': 0.15,
    'suitability_to_weather_type': 0.1,
    'suitability_to_time_of_the_day': 0.1,
    'suitability_to_event_type': 0.2,
    'spatial_resolution': 0.15,
    'frequency_of_update': 0.15,
    'cost': 0.15,
    'price': 0.20,
    'data_quality': 0.1

}

def api_call_to_get_the_arrival_time_of_satellite(centroid):
    time_in_utc = 1
    #todo: get arrival time in utc @Alberto
    return time_in_utc


def get_suitability_to_weather_rating(satellite_id,weather_details):
    weather_rating = 0
    #todo: do the rating logic according to the lookup table
    return weather_rating

def get_suitability_to_time_of_day_rating(satellite_name,arrival_time_of_satellite):
    #todo: do the rating logic according to the lookup table
    time_of_day_rating = 0
    return time_of_day_rating


def get_spatial_resolution_rating(satellite_name):
    #todo: do the rating logic according to the lookup table
    spatial_resolution_rating = 0
    return spatial_resolution_rating
    
    

def get_cost_rating(satellite_name):
    #todo: do the rating logic according to the lookup table
    cost_rating = 0
    return cost_rating
        
    
def get_freequency_of_update_rating(satellite_name):
    #todo: do the rating logic according to the lookup table
    freequency_of_update_rating = 0
    return freequency_of_update_rating
        

def get_price_rating(satellite_name):
    #todo: do the rating logic according to the lookup table
    price_rating = 0
    return price_rating    

def get_data_quality_rating(satellite_name):
    #todo: do the rating logic according to the lookup table
    data_quality_rating = 0
    return data_quality_rating   



def rank_satellites(subarea, list_of_satellite, weather_details, event_type):
    filtered_satellites = []
    for satellite in list_of_satellite:
        if subarea["centroid"]:
          time_now = datetime.datetime.utcnow()  
          arrival_time_of_satellite = api_call_to_get_the_arrival_time_of_satellite (satellite["id"],subarea["centroid"])
          timeliness_rating = 10*(1-arrival_time_of_satellite/satellite["orbitDuration"])
        else: 
            raise Exception("Sorry, no centroid in the input.")

        suitability_to_event_rating=0
        if event_type in satellite["eventTypes"]:
            suitability_to_event_rating=10

        suitability_to_weather_rating=0
        suitability_to_weather_rating= get_suitability_to_weather_rating(satellite["name"],weather_details)   

        suitability_to_time_of_day_rating = 0
        suitability_to_time_of_day_rating= get_suitability_to_time_of_day_rating(satellite["name"],arrival_time_of_satellite)   

        spatial_resolution_rating = 0
        spatial_resolution_rating= get_spatial_resolution_rating(satellite["name"])        

        cost_rating = 0
        cost_rating= get_cost_rating(satellite["name"])  

        freequency_of_update_rating = 0
        freequency_of_update_rating= get_freequency_of_update_rating(satellite["name"])      
        
        price_rating = 0
        price_rating = get_price_rating(satellite["name"]) 

        data_quality_rating = 0
        data_quality_rating = get_data_quality_rating(satellite["name"])   

        overall_rating = (weight_dict["timeliness"]*timeliness_rating) + (weight_dict["suitability_to_weather_type"]*suitability_to_weather_rating) + (weight_dict["suitability_to_time_of_the_day"]*suitability_to_time_of_day_rating) + (weight_dict["suitability_to_event_type"]*suitability_to_event_rating) + (weight_dict["spatial_resolution"]*spatial_resolution_rating) + (weight_dict["frequency_of_update"]*freequency_of_update_rating) + (weight_dict["cost"]*cost_rating) + (weight_dict["price"]*price_rating) + (weight_dict["data_quality"]* data_quality_rating)

        satelite_object_with_all_ratings={
            "name":satellite["name"],
            "timeliness":timeliness_rating,
            "suitability_to_weather_type":suitability_to_weather_rating,
            "suitability_to_time_of_the_day":suitability_to_time_of_day_rating,
            "suitability_to_event_type":suitability_to_event_rating,
            "geographical_definition":spatial_resolution_rating,
            "frequency_of_update":freequency_of_update_rating,
            "cost":cost_rating,
            "price":price_rating,
            "data_quality":data_quality_rating,
            "overall_rating":overall_rating

        }
        filtered_satellites = filtered_satellites.append(satelite_object_with_all_ratings)

    sorted_satellite_objects = sorted(filtered_satellites, key=lambda x: x['overall_rating'], reverse=True)

    return sorted_satellite_objects
