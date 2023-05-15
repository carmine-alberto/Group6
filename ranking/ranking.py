import datetime

from localdata import master_satellites
master_satellites_list = master_satellites

from views import calculate_travel_time


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

def api_call_to_get_the_arrival_time_duartion_of_satellite(satellite,subarea):
    calculate_travel_time(satellite,subarea)
    time_in_utc = 1
    #todo: get arrival time in utc @Alberto

    return time_in_utc


def get_suitability_to_event_rating(satellite,event_type):
    suitability_to_event_rating=0
    if event_type in [e.name for e in satellite["eventTypes"]]:
        suitability_to_event_rating=10
    return  suitability_to_event_rating

def get_suitability_to_weather_rating(satellite,weather_details):
    visibility_threshold = satellite["visibility_threshold"]
    visibility = weather_details["visibility"]
    weather_rating = visibility - (1 - visibility_threshold)
    return weather_rating

def get_suitability_to_time_of_day_rating(satellite,weather_details):
    time_of_day_rating=5
    if weather_details['isDay']==True or satellite["worksDuringNight"]==True: 
        time_of_day_rating = 10
    elif satellite["worksDuringNight"]==False and weather_details['isDay']==False:  
        time_of_day_rating = 0
    return time_of_day_rating


def get_spatial_resolution_rating(satellite):
    spatial_resolution_rating = satellite['spatialResolution']
    return spatial_resolution_rating
    
    

def get_cost_rating(satellite):
    #todo: do the rating logic according to group 7
    cost_rating = satellite["cost"]
    return cost_rating
        
    
def get_freequency_of_update_rating(satellite):
    #todo: do the rating logic according to the lookup table
    freequency_of_update_rating = satellite["freequencyOfUpdateRating"]
    return freequency_of_update_rating
        

def get_price_rating(satellite):
    #todo: do the rating logic according to the lookup table
    price_rating = satellite["priceRating"]
    return price_rating    

def get_data_quality_rating(satellite):
    #todo: do the rating logic according to the lookup table
    data_quality_rating = satellite["dataQualityRating"]
    return data_quality_rating   



def rank_satellites(subarea, weather_details, event_type):
    filtered_satellites = []
    for satellite in master_satellites_list:
        if subarea["centroid"]:
          time_now = datetime.datetime.utcnow()  
          arrival_duration_of_satellite = api_call_to_get_the_arrival_time_duartion_of_satellite(satellite,subarea)
          timeliness_rating = 10*(1-arrival_duration_of_satellite/satellite["orbitDuration"])
        else: 
            raise Exception("Sorry, no centroid in the input.")

       
        suitability_to_event_rating=0
        suitability_to_event_rating= get_suitability_to_event_rating(satellite,event_type)               

        suitability_to_weather_rating=0
        suitability_to_weather_rating= get_suitability_to_weather_rating(satellite,weather_details)   

        suitability_to_time_of_day_rating = 0
        suitability_to_time_of_day_rating= get_suitability_to_time_of_day_rating(satellite,weather_details)   

        spatial_resolution_rating = 0
        spatial_resolution_rating= get_spatial_resolution_rating(satellite)        

        cost_rating = 0
        cost_rating= get_cost_rating(satellite)  

        freequency_of_update_rating = 0
        freequency_of_update_rating= get_freequency_of_update_rating(satellite)      
        
        price_rating = 0
        price_rating = get_price_rating(satellite) 

        data_quality_rating = 0
        data_quality_rating = get_data_quality_rating(satellite)   

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
