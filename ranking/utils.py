import json
from datetime import datetime


def parse_body():
    with open('../example.json', 'r') as file:
        json_dict = json.load(file)

        return json_dict

def get_timestamp(string, date_format = "%Y-%m-%dT%H:%M"):
    return datetime.strptime(string, date_format)

def interpolate(left_val, right_val, weight):
    return left_val * weight + right_val * (1-weight)






