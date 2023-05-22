from enum import Enum

NASA = False

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
        #completed
        "family": "Modis",
        "name": "Aqua",
        "id": "27424",
        "apiName": "https://planetarycomputer.microsoft.com/api/stac/v1",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.VOLCANIC_ERUPTION],
        "visibility_threshold": 0.7,    
        "spatialResolution": 250,
        "frequencyOfUpdate": 0.5,
        "swathWidth": 2.330, #in km
        "orbitDuration": "76000", #should be in seconds - It could be found using tle.period
        "worksDuringNight": True, 
        "worksDuringDay": True, 
        "price": 6, #group 7
        "dataQualityRating": 10
    },
    {   #completed
        "family": "Modis",
        "name": "Terra",
        "id": "25994",
        "apiName": "https://planetarycomputer.microsoft.com/api/stac/v1",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.VOLCANIC_ERUPTION, eventTypes.STORM],
        "visibility_threshold": 0.7,    
        "spatialResolution": 250,
        "frequencyOfUpdate": 1,
        "swathWidth": 2330, #in km
        "orbitDuration": "", #should be in seconds - It could be found using tle.period
        "worksDuringNight": True,
        "worksDuringDay": True, 
        "price": 6, #group 7
        "dataQualityRating": 10
    },
    {   
        #completed
        "family": "Sentinel",
        "name": "Sentinel-1A",
        "id": "39634",
        "apiName": "https://planetarycomputer.microsoft.com/api/stac/v1",
        "eventTypes": [eventTypes.FLOOD, eventTypes.EARTHQUAKE, eventTypes.OIL_SPILL],
        "visibility_threshold": 0,
        "spatialResolution": 5,
        "frequencyOfUpdate": 6,
        "swathWidth": 250, #km
        "orbitDuration": "", #with the function
        "worksDuringNight": True, 
        "worksDuringDay": False, 
        "price": 0, #from group 7
        "dataQualityRating": 10
    },
    {   
        #completed
        "family": "Sentinel",
        "name": "Sentinel-5P", #It's actually S-2 but maybe it's not supported
        "id": "40697",
        "apiName": "https://planetarycomputer.microsoft.com/api/stac/v1",
        "eventTypes": [eventTypes.FIRE, eventTypes.FLOOD, eventTypes.VOLCANIC_ERUPTION, eventTypes.OIL_SPILL],
        "visibility_threshold": 0.9,
        "spatialResolution": 10,
        "frequencyOfUpdate": 5,
        "swathWidth": 290,
        "orbitDuration": "", #with the function
        "worksDuringNight": False, 
        "worksDuringDay": True, 
        "price": 0,
        "dataQualityRating": 10
    },
    {
        #completed
        "family": "Sentinel",
        "name": "Sentinel-3A",
        "id": "41335",
        "apiName": "https://planetarycomputer.microsoft.com/api/stac/v1",
        "eventTypes": [eventTypes.STORM, eventTypes.TSUNAMI],
        "visibility_threshold": 0.9,
        "spatialResolution": 300,
        "frequencyOfUpdate": 1,
        "swathWidth": 1270,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True, 
        "price": 0,
        "dataQualityRating": 10
    },
    {
        #completed
        "family": "Landsat",
        "name": "Landsat-8",
        "id": "39084",
        "apiName": "https://planetarycomputer.microsoft.com/api/stac/v1",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.VOLCANIC_ERUPTION],
        "visibility_threshold": 0.7,
        "spatialResolution": 15,
        "frequencyOfUpdate": 16,
        "swathWidth": 185,
        "orbitDuration": "", #with the function
        "worksDuringNight": False,
        "worksDuringDay": True, 
        "price": 0,
        "dataQualityRating": 10
    },
    {
        #completed
        "family": "Eros",
        "name": "EOS-Aura", #Eros-B", not supported
        "id": "29079",
        "apiName": "https://planetarycomputer.microsoft.com/api/stac/v1", #or "apiName": "https://apollomapping.com/buy-imagery",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.OIL_SPILL],
        "visibility_threshold": 0.7,
        "spatialResolution": 0.7,
        "frequencyOfUpdate": 4,
        "swathWidth": 12,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True, 
        "price": 6,
        "dataQualityRating": 10
    },
    {
        #completed
        "family": "Planet",
        "name": "landsat-7", # SKYSAT-A",
        "id": "39418",
        "apiName": "https://www.planet.com/contact-sales/",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.8,
        "spatialResolution": 1,
        "frequencyOfUpdate": 1, 
        "swathWidth": 10,
        "orbitDuration": "", #with the function
        "worksDuringNight": True, 
        "worksDuringDay": True, 
        "price": 14,
        "dataQualityRating": 10
    },

    {   
        #completed
        "family": "Maxar",
        "name": "NOAA-16", #WORLDVIEW-1 (WV-1)",
        "id": "32060",
        "apiName": "https://securewatch.maxar.com/mapservice",
        "eventTypes": [eventTypes.EARTHQUAKE, eventTypes.FLOOD, eventTypes.FIRE, eventTypes.OIL_SPILL, eventTypes.TSUNAMI],
        "eventTypes": [eventTypes.EARTHQUAKE, eventTypes.FLOOD, eventTypes.FIRE, eventTypes.OIL_SPILL, eventTypes.TSUNAMI],
        "visibility_threshold": 0.3,
        "spatialResolution": 0.5,
        "frequencyOfUpdate": 1,
        "swathWidth": 17.6,
        "orbitDuration": "", #with the function
        "worksDuringNight": True, 
        "worksDuringDay": True, 
        "price": 20,
        "dataQualityRating": 10
    },
    {
        #i don't know the swath width
        "family": "Airbus",
        "name": "SPOT-6", #ONEWEB-0066",
        "id": "45424",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.3,
        "spatialResolution": 0.5,
        "frequencyOfUpdate": 1,
        "swathWidth": "",
        "orbitDuration": "", #with the function
        "worksDuringNight": True, 
        "worksDuringDay": True, 
        "price": 12.5,
        "dataQualityRating": 10
    }
]

#TODO Remove comments when the list is ready
#TODO @Giulia check worksDuringNight and worksDuringDay values

'''
    {
        #completed
        "family": "Planet",
        "name": "SKYSAT-B",
        "id": "40072",
        "apiName": "https://www.planet.com/contact-sales/",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.2,
        "spatialResolution": 0.75,
        "frequencyOfUpdate": 1,
        "swathWidth": 10, 
        "orbitDuration": "", #with the function
        "worksDuringNight": True, #and also during day
        "price": 14,
        "dataQualityRating": 10
    },
    {   
        #from now on all the satelittes of PLANET are copied from SKYSAT-B
        "family": "Planet",
        "name": "SKYSAT-C1",
        "id": "41601",
        "apiName": "https://www.planet.com/contact-sales/",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.2,
        "spatialResolution": 0.75,
        "frequencyOfUpdate": 1,
        "swathWidth": 10, 
        "orbitDuration": "", #with the function
        "worksDuringNight": True, #and also during day
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-C4",
        "id": "41771",
        "apiName": "https://www.planet.com/contact-sales/",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.2,
        "spatialResolution": 0.75,
        "frequencyOfUpdate": 1,
        "swathWidth": 10, 
        "orbitDuration": "", #with the function
        "worksDuringNight": True, #and also during day
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-C13",
        "id": "43802",
        "apiName": "https://www.planet.com/contact-sales/",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.2,
        "spatialResolution": 0.75,
        "frequencyOfUpdate": 1,
        "swathWidth": 10, 
        "orbitDuration": "", #with the function
        "worksDuringNight": True, #and also during day
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-C14",
        "id": "45788",
        "apiName": "https://www.planet.com/contact-sales/",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.2,
        "spatialResolution": 0.75,
        "frequencyOfUpdate": 1,
        "swathWidth": 10, 
        "orbitDuration": "", #with the function
        "worksDuringNight": True, #and also during day
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-C16",
        "id": "45789",
        "apiName": "https://www.planet.com/contact-sales/",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.2,
        "spatialResolution": 0.75,
        "frequencyOfUpdate": 1,
        "swathWidth": 10, 
        "orbitDuration": "", #with the function
        "worksDuringNight": True, #and also during day
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-C15",
        "id": "45790",
        "apiName": "https://www.planet.com/contact-sales/",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.2,
        "spatialResolution": 0.75,
        "frequencyOfUpdate": 1,
        "swathWidth": 10, 
        "orbitDuration": "", #with the function
        "worksDuringNight": True, #and also during day
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-C5",
        "id": "41772",
        "apiName": "https://www.planet.com/contact-sales/",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.2,
        "spatialResolution": 0.75,
        "frequencyOfUpdate": 1,
        "swathWidth": 10, 
        "orbitDuration": "", #with the function
        "worksDuringNight": True, #and also during day
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-C3",
        "id": "41774",
        "apiName": "https://www.planet.com/contact-sales/",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.2,
        "spatialResolution": 0.75,
        "frequencyOfUpdate": 1,
        "swathWidth": 10, 
        "orbitDuration": "", #with the function
        "worksDuringNight": True, #and also during day
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-C11",
        "id": "42987",
        "apiName": "https://www.planet.com/contact-sales/",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.2,
        "spatialResolution": 0.75,
        "frequencyOfUpdate": 1,
        "swathWidth": 10, 
        "orbitDuration": "", #with the function
        "worksDuringNight": True, #and also during day
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-C10",
        "id": "42988",
        "apiName": "https://www.planet.com/contact-sales/",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.2,
        "spatialResolution": 0.75,
        "frequencyOfUpdate": 1,
        "swathWidth": 10, 
        "orbitDuration": "", #with the function
        "worksDuringNight": True, #and also during day
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-C9",
        "id": "42989",
        "apiName": "https://www.planet.com/contact-sales/",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.2,
        "spatialResolution": 0.75,
        "frequencyOfUpdate": 1,
        "swathWidth": 10, 
        "orbitDuration": "", #with the function
        "worksDuringNight": True, #and also during day
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-C8",
        "id": "42990",
        "apiName": "https://www.planet.com/contact-sales/",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.2,
        "spatialResolution": 0.75,
        "frequencyOfUpdate": 1,
        "swathWidth": 10, 
        "orbitDuration": "", #with the function
        "worksDuringNight": True, #and also during day
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-C7",
        "id": "42991",
        "apiName": "https://www.planet.com/contact-sales/",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.2,
        "spatialResolution": 0.75,
        "frequencyOfUpdate": 1,
        "swathWidth": 10, 
        "orbitDuration": "", #with the function
        "worksDuringNight": True, #and also during day
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-C6",
        "id": "42992",
        "apiName": "https://www.planet.com/contact-sales/",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.2,
        "spatialResolution": 0.75,
        "frequencyOfUpdate": 1,
        "swathWidth": 10, 
        "orbitDuration": "", #with the function
        "worksDuringNight": True, #and also during day
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-C12",
        "id": "43797",
        "apiName": "https://www.planet.com/contact-sales/",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.2,
        "spatialResolution": 0.75,
        "frequencyOfUpdate": 1,
        "swathWidth": 10, 
        "orbitDuration": "", #with the function
        "worksDuringNight": True, #and also during day
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-C17",
        "id": "46179",
        "apiName": "https://www.planet.com/contact-sales/",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.2,
        "spatialResolution": 0.75,
        "frequencyOfUpdate": 1,
        "swathWidth": 10, 
        "orbitDuration": "", #with the function
        "worksDuringNight": True, #and also during day
        "price": 14,
        "dataQualityRating": 10
    }
    '''

'''
{
    #from now on these are copied from the before one
    "family": "Airbus",
    "name": "ONEWEB-0305",
    "id": "70305",
    "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive   ",
    "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.5,
    "frequencyOfUpdate": 1,
    "swathWidth": "",
    "orbitDuration": "", #with the function
    "worksDuringNight": True, #also during day
    "price": 12.5,
    "dataQualityRating": 10
},
{
    "family": "Airbus",
    "name": "ONEWEB-0432",
    "id": "50502",
    "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
    "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.5,
    "frequencyOfUpdate": 1,
    "swathWidth": "",
    "orbitDuration": "", #with the function
    "worksDuringNight": True, #also during day
    "price": 12.5,
    "dataQualityRating": 10
},
{
    "family": "Airbus",
    "name": "ONEWEB-0058",
    "id": "45161",
    "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
    "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.5,
    "frequencyOfUpdate": 1,
    "swathWidth": "",
    "orbitDuration": "", #with the function
    "worksDuringNight": True, #also during day
    "price": 12.5,
    "dataQualityRating": 10
},
{
    "family": "Airbus",
    "name": "ONEWEB-0303",
    "id": "70303",
    "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
    "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.5,
    "frequencyOfUpdate": 1,
    "swathWidth": "",
    "orbitDuration": "", #with the function
    "worksDuringNight": True, #also during day
    "price": 12.5,
    "dataQualityRating": 10
},
{
    "family": "Airbus",
    "name": "ONEWEB-0107",
    "id": "48048",
    "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
    "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.5,
    "frequencyOfUpdate": 1,
    "swathWidth": "",
    "orbitDuration": "", #with the function
    "worksDuringNight": True, #also during day
    "price": 12.5,
    "dataQualityRating": 10
},
{
    "family": "Airbus",
    "name": "ONEWEB-0053",
    "id": "45157",
    "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
    "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.5,
    "frequencyOfUpdate": 1,
    "swathWidth": "",
    "orbitDuration": "", #with the function
    "worksDuringNight": True, #also during day
    "price": 12.5,
    "dataQualityRating": 10
},
{
    "family": "Airbus",
    "name": "ONEWEB-0032",
    "id": "45141",
    "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
    "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.5,
    "frequencyOfUpdate": 1,
    "swathWidth": "",
    "orbitDuration": "", #with the function
    "worksDuringNight": True, #also during day
    "price": 12.5,
    "dataQualityRating": 10
},
{
    "family": "Airbus",
    "name": "ONEWEB-0012",
    "id": "44057",
    "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
    "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.5,
    "frequencyOfUpdate": 1,
    "swathWidth": "",
    "orbitDuration": "", #with the function
    "worksDuringNight": True, #also during day
    "price": 12.5,
    "dataQualityRating": 10
},
{
    "family": "Airbus",
    "name": "ONEWEB-0063",
    "id": "45448",
    "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
    "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.5,
    "frequencyOfUpdate": 1,
    "swathWidth": "",
    "orbitDuration": "", #with the function
    "worksDuringNight": True, #also during day
    "price": 12.5,
    "dataQualityRating": 10
},
{
    "family": "Airbus",
    "name": "ONEWEB-0064",
    "id": "45433",
    "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
    "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.5,
    "frequencyOfUpdate": 1,
    "swathWidth": "",
    "orbitDuration": "", #with the function
    "worksDuringNight": True, #also during day
    "price": 12.5,
    "dataQualityRating": 10
},
{
    "family": "Airbus",
    "name": "ONEWEB-0054",
    "id": "45158",
    "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
    "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.5,
    "frequencyOfUpdate": 1,
    "swathWidth": "",
    "orbitDuration": "", #with the function
    "worksDuringNight": True, #also during day
    "price": 12.5,
    "dataQualityRating": 10
},
{
    "family": "Airbus",
    "name": "ONEWEB-0033",
    "id": "45142",
    "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
    "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.5,
    "frequencyOfUpdate": 1,
    "swathWidth": "",
    "orbitDuration": "", #with the function
    "worksDuringNight": True, #also during day
    "price": 12.5,
    "dataQualityRating": 10
},
{
    "family": "Airbus",
    "name": "ONEWEB-0010",
    "id": "44058",
    "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
    "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.5,
    "frequencyOfUpdate": 1,
    "swathWidth": "",
    "orbitDuration": "", #with the function
    "worksDuringNight": True, #also during day
    "price": 12.5,
    "dataQualityRating": 10
},
{
    "family": "Airbus",
    "name": "ONEWEB-0019",
    "id": "45449",
    "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
    "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.5,
    "frequencyOfUpdate": 1,
    "swathWidth": "",
    "orbitDuration": "", #with the function
    "worksDuringNight": True, #also during day
    "price": 12.5,
    "dataQualityRating": 10
},
{
    "family": "Airbus",
    "name": "ONEWEB-0018",
    "id": "45434",
    "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
    "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.5,
    "frequencyOfUpdate": 1,
    "swathWidth": "",
    "orbitDuration": "", #with the function
    "worksDuringNight": True, #also during day
    "price": 12.5,
    "dataQualityRating": 10
},
{
    "family": "Airbus",
    "name": "ONEWEB-0056",
    "id": "45159",
    "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
    "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.5,
    "frequencyOfUpdate": 1,
    "swathWidth": "",
    "orbitDuration": "", #with the function
    "worksDuringNight": True, #also during day
    "price": 12.5,
    "dataQualityRating": 10
},
{
    "family": "Airbus",
    "name": "ONEWEB-0035",
    "id": "45143",
    "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
    "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.5,
    "frequencyOfUpdate": 1,
    "swathWidth": "",
    "orbitDuration": "", #with the function
    "worksDuringNight": True, #also during day
    "price": 12.5,
    "dataQualityRating": 10
},
{
    "family": "Airbus",
    "name": "ONEWEB-0008",
    "id": "44059",
    "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
    "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.5,
    "frequencyOfUpdate": 1,
    "swathWidth": "",
    "orbitDuration": "", #with the function
    "worksDuringNight": True, #also during day
    "price": 12.5,
    "dataQualityRating": 10
}
'''

'''
{
    #i don't know frequency of update
    "family": "Maxar",
    "name": "WORLDVIEW-2 (WV-2)",
    "id": "35946",
    "apiName": "https://securewatch.maxar.com/mapservice",
    "eventTypes": [eventTypes.EARTHQUAKE, eventTypes.FLOOD, eventTypes.FIRE, eventTypes.OIL_SPILL, eventTypes.TSUNAMI],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.46,
    "frequencyOfUpdate": 1,
    "swathWidth": 16.4,
    "orbitDuration": "", #with the function
    "worksDuringNight": False, 
    "price": 20,
    "dataQualityRating": 10
},
{
    #i don't know frequency of update
    "family": "Maxar",
    "name": "WORLDVIEW-3 (WV-3)",
    "id": "40115",
    "apiName": "https://securewatch.maxar.com/mapservice",
    "eventTypes": [eventTypes.EARTHQUAKE, eventTypes.FLOOD, eventTypes.FIRE, eventTypes.OIL_SPILL, eventTypes.TSUNAMI],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.31,
    "frequencyOfUpdate": 1,
    "swathWidth": 13.1,
    "orbitDuration": "", #with the function
    "worksDuringNight": False, 
    "price": 20,
    "dataQualityRating": 10
},
{ 
    #i don't know frequency of update
    "family": "Maxar",
    "name": "WORLDVIEW-4",
    "id": "41848",
    "apiName": "https://securewatch.maxar.com/mapservice",
    "eventTypes": [eventTypes.EARTHQUAKE, eventTypes.FLOOD, eventTypes.FIRE, eventTypes.OIL_SPILL, eventTypes.TSUNAMI],
    "visibility_threshold": 0.3,
    "spatialResolution": 0.31,
    "frequencyOfUpdate": 1,
    "swathWidth": 13.1,
    "orbitDuration": "", #with the function
    "worksDuringNight": False, 
    "price": 20,
    "dataQualityRating": 10
},
'''