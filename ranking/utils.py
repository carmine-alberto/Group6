import json

from geohash import geohash

def parse_body():
    with open('../example.json', 'r') as file:
        json_dict = json.load(file)

    body = geohash.decode(json_dict[0]["sxk"])






