from pyorbital import tlefile
from pyorbital.orbital import Orbital
from datetime import datetime, timedelta
from math import sqrt

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
## TODO Check Varun is passing the right parameters in his calls

# ENSURES
## The arrival time (UTC) if the satellite is going to cross the target location
## -1 if it's never going to cross the target location
def calculate_travel_time(satellite_data, target_location):
    # Specify the TLE data for the satellite
    tle = Orbital(
        satellite_data["name"],
        satellite_data["line1"],
        satellite_data["line2"]
    )  # TODO FIX

    # Specify the desired location
    lat = target_location["lat"]  # New York City latitude
    lon = target_location["lon"]  # New York City longitude
    alt = target_location["alt"]  # Altitude in km

    # Calculate the time required for the satellite to reach the specified location
    dt = 300  # Time interval in seconds - TODO What is the LSB we want to use?
    time = datetime.utcnow()
    now = time

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

