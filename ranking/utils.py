import json
import Geohash

def parse_body():
    with open('../example.json', 'r') as file:
        json_dict = json.load(file)

    body = Geohash.decode(json_dict[0]["sxk"])

    #Use pandas to handle body maybe?






