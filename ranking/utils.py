import json
from datetime import datetime

import dateutil

HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

def parse_body(json_data):
    return json.loads(json_data)
def parse_file():
    with open('group5_output.json', 'r') as file:
        json_dict = json.load(file)

        return json_dict

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

