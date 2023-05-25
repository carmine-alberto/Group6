import json
import geohash
from datetime import datetime
import itertools

import dateutil

HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

def parse_body(json_data):
    return json.loads(json_data)
def parse_file():
    with open('group5_output.json', 'r') as file:
        return json.load(file)

#TODO These 2 are not working as expected. Please check them in a branch, not using them for now
def extract_values(data, keys):
    values = []
    if isinstance(data, dict):
        for key, value in data.items():
            if key in keys:
                values.append({key:value})
            if isinstance(value, (dict, list)):
                values.extend(extract_values(value, keys))
    elif isinstance(data, list):
        for item in data:
            values.extend(extract_values(item, keys))
    return values

def parse_body_flatten(json_data):
    return json.loads(json_data)

def parse_file_flatten():
    with open('example.json', 'r') as file:
        json_dict = json.load(file)
        keys_dict = list(itertools.chain.from_iterable(x for x in json_dict))
        result = extract_values(json_dict, keys_dict)
    # I am extracting into a file to check just use result finally
    output_file = "flat.json"
    with open(output_file, "w") as file:
        json.dump(result, file)

    return result # I have already done it 

def get_timestamp(string, date_format = "%Y-%m-%dT%H:%M"):
    return datetime.strptime(string, date_format)

def interpolate(left_val, right_val, weight):
    return left_val * weight + right_val * (1-weight)

def validate_date(date):
    try:
        dateutil.parser.parse(date)
        return True
    except Exception as e:
        return False

    
def extract_polygon_from_geohash(geo_hash_str):
    bounding_box = geohash.bbox(geo_hash_str)
    min_lat = bounding_box["e"]
    max_lat = bounding_box["w"]
    min_lon = bounding_box["s"]
    max_lon = bounding_box["n"]

    # Create a polygon from the bounding box coordinates
    polygon_bb = [[[min_lat, min_lon], [min_lat, max_lon], [max_lat, max_lon], [max_lat, min_lon]]]

    return polygon_bb


