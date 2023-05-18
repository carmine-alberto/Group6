from pyorbital import tlefile
from pyorbital.orbital import Orbital
from pyorbital import astronomy
from datetime import datetime, timedelta
from math import sqrt
from math import radians

# REQUIRES
# satelliteData
## key1: name
## key2: line1
## key3: line2
## key4: minimumSnapshotArea
## key5: orbitDuration

# targetLocation - API request to group 5 to obtain the event location
## key1: lat
## key2: lon
## key3: alt

# ENSURES
## The arrival time (UTC) if the satellite is going to cross the target location
## The orbit period
def calculate_travel_time_and_orbit_duration(satellite_data, target_location, timestamp):
    # Specify the TLE data for the satellite
    tle = Orbital(
        satellite_data["name"],
        None,
        None, #satellite_data["line1"],
        None, #satellite_data["line2"]
    )

    # Specify the desired location
    lat = float(target_location["lat"]) # New York City latitude
    lon = float(target_location["lon"]) # New York City longitude
    alt = float(target_location["alt"]) # Altitude in km

    # Calculate the time required for the satellite to reach the specified location
    #dt = 300  # Time interval in seconds - TODO What is the LSB we want to use? - USED FOR A DIFFERENT ALGO, read below
    time = timestamp
    orbitPeriod = tle.orbit_elements.period #Assumption: it's in hours TODO CHECK
    orbitPeriodInHours = orbitPeriod / 60
    orbitPeriodInSeconds = orbitPeriod * 60

    next_pass_list = tle.get_next_passes(time, int(orbitPeriod + 5), lon, lat, alt, 1)

    #First element of the array as it's the closest in time; third of the tuple as it's the maximum-distance position
    delta = next_pass_list[0][2] - time

    return delta.total_seconds(), orbitPeriodInSeconds
    '''
    now = time

    #Currently using built-in get_next_passes library function 
    orbit_duration = float(satellite_data["orbitDuration"])
    dt_per_orbit = orbit_duration / dt
    minimum_snapshot_area = float(satellite_data["minimumSnapshotArea"])

    while dt_per_orbit > 0:
        
        pos, _ = tle.get_position(time)
        dist = pos.distance_from(lat, lon, alt) #TODO check format. Is it comparable with snapshot_area?
        # Here, we should consider the area size too. If it's too large, there could be some pieces missing
        if dist < sqrt(minimum_snapshot_area):  # If satellite is within 5 km of the location, break out of the loop - TODO the threshold is selected by picking the square root of the minimum snapshot area
            return time - now
        time += timedelta(seconds=dt)
        dt_per_orbit -= 1

    # Done like this because of the formula in the rating algorithm: 10(1 - delta/orbitDuration) -> 0 if no match is found
    return orbit_duration
    '''



