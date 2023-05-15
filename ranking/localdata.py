from enum import Enum


class eventTypes(Enum):

    FLOOD = 1
    FIRE = 2
    VOLCANIC_ERUPTION = 3
    EARTHQUAKE = 4
    OIL_SPILL = 5
    STORM = 6
    TSUNAMI = 7
    


master_satellites = [
    {
        "family": "",
        "name": "Modis",
        "id": "",
        "apiName": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.VOLCANIC_ERUPTION],
        "visibility_threshold": 0.3,
        "spatialResolution": 250,
        "cost": "",
        "frequencyOfUpdate": 0.5,
        "minimumSnapshotArea": "",
        "orbitDuration": ""
    },
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
        "family": "",
        "name": "Airbus",
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
        "family": "",
        "name": "Eros-B",
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
        "family": "",
        "name": "Maxar",
        "id": "",
        "apiName": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.STORM],
        "visibility_threshold": 0.3,
        "spatialResolution": 0.3,
        "cost": "",
        "frequencyOfUpdate": 1,
        "minimumSnapshotArea": "",
        "orbitDuration": ""
    },

]

