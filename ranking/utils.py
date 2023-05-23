import json

def parse_body():
    with open('../example.json', 'r') as file:
        json_dict = json.load(file)

        return json_dict








