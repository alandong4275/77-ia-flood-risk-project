from utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples of stations with latest relative water levels over tol and their relative water levels"""
    
    s_over_threshold = []
    for station in stations:
        if station.latest_level != None:
            if station.typical_range_consistent():
                if station.relative_water_level() > tol:
                    s_over_threshold.append((station, station.relative_water_level()))

    sorted_list = sorted_by_key(s_over_threshold, 1)
    return sorted_list

def stations_highest_rel_level(stations, N):
    """returns a list of the N stations at which the water level, relative to the typical range, is highest"""

    stationsWithHightWater = []
    for station in stations:
        stationsWithHightWater.append((stations.station_id, station.relative_water_level()))
    
    sortedlist = sorted_by_key(stationsWithHightWater, 1, reverse = True)[:N]

    return sortedlist