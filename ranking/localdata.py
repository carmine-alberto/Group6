from enum import Enum


class eventTypes(Enum):

    FLOOD = 1
    FIRE = 2
    VOLCANIC_ERUPTION = 3
    EARTHQUAKE = 4
    OIL_SPILL = 5
    STORM = 6
    TSUNAMI = 7
    

weights = {
    'timeliness': 10,
    'suitability_to_weather_type': 8,
    'suitability_to_time_of_the_day': 8,
    'suitability_to_event_type': 8,
    'spatial_resolution': 6,
    'frequency_of_update': 1,
    'price': 7,
    'data_quality': 3

}

master_satellites = [
    {
        "family": "Modis",
        "name": "Aqua",
        "id": "27424",
        "apiName": "https://randomAPI.org", #TODO get from group7
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.VOLCANIC_ERUPTION],
        "visibility_threshold": 0.3,
        "spatialResolution": 250,
        "frequencyOfUpdate": 0.5,
        "minimumSnapshotArea": 100, #in km
        "orbitDuration": "36000", #should be in seconds
        "worksDuringNight": True, #TODO add for others as well @Olmar
        "price": 10, #TODO add for others as well @Olmar also ask for group 7 for this
        "dataQualityRating": 1
    }
    ]
'''
    {
        "family": "",
        "name": "Sentinel 1",
        "id": "",
        "apiName": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.EARTHQUAKE, eventTypes.OIL_SPILL],
        "visibility_threshold": 1,
        "spatialResolution": 5,
        "cost": "",
        "frequencyOfUpdate": 6,
        "minimumSnapshotArea": "",
        "orbitDuration": ""
    },
    {
        "family": "",
        "name": "Sentinel 2",
        "id": "",
        "apiName": "",
        "eventTypes": [eventTypes.FIRE, eventTypes.FLOOD, eventTypes.VOLCANIC_ERUPTION, eventTypes.OIL_SPILL],
        "visibility_threshold": 0.1,
        "spatialResolution": 10,
        "cost": "",
        "frequencyOfUpdate": 5,
        "minimumSnapshotArea": "",
        "orbitDuration": ""
    },
    {
        "family": "",
        "name": "Sentinel 3",
        "id": "",
        "apiName": "",
        "eventTypes": [eventTypes.STORM, eventTypes.TSUNAMI],
        "visibility_threshold": 0.1,
        "spatialResolution": 300,
        "cost": "",
        "frequencyOfUpdate": 1,
        "minimumSnapshotArea": "",
        "orbitDuration": ""
    },
    {
        "family": "",
        "name": "Landsat 8",
        "id": "",
        "apiName": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.VOLCANIC_ERUPTION],
        "visibility_threshold": 0.3,
        "spatialResolution": 15,
        "cost": "",
        "frequencyOfUpdate": 16,
        "minimumSnapshotArea": "",
        "orbitDuration": ""
    },
    {
        "family": "",
        "name": "Planet",
        "id": "",
        "apiName": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.STORM],
        "visibility_threshold": 0.8,
        "spatialResolution": 3.7,
        "cost": "",
        "frequencyOfUpdate": 1,
        "minimumSnapshotArea": "",
        "orbitDuration": ""
    },
    {
        "family": "Airbus",
        "name": "",
        "id": "",
        "apiName": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.VOLCANIC_ERUPTION],
        "visibility_threshold": 0.3,
        "spatialResolution": 0.5,
        "cost": "",
        "frequencyOfUpdate": 1,
        "minimumSnapshotArea": "",
        "orbitDuration": ""
    },
    {
        "family": "Eros-B",
        "name": "",
        "id": "",
        "apiName": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.OIL_SPILL],
        "visibility_threshold": 0.3,
        "spatialResolution": 0.7,
        "cost": "",
        "frequencyOfUpdate": 4,
        "minimumSnapshotArea": "",
        "orbitDuration": ""
    },
    {
        "family": "Maxar",
        "name": "",
        "id": "",
        "apiName": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.STORM],
        "visibility_threshold": 0.3,
        "spatialResolution": 0.3,
        "cost": "",
        "frequencyOfUpdate": 1,
        "minimumSnapshotArea": "",
        "orbitDuration": ""
    }

]
#TODO Remove comments when the list is ready
'''
