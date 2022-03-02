from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples of stations with latest relative water levels over tol and their relative water levels"""
    # iterates over all the stations adding to a list stations with greater relative water level than tolerance
    # but skips stations with no data and checks the data is consistent with itself
    s_over_threshold = []
    for station in stations:
        if station.latest_level != None:
            if station.typical_range_consistent():
                if station.relative_water_level() > tol:
                    s_over_threshold.append((station, station.relative_water_level()))
    #sorts the list by relative water level
    sorted_list = sorted_by_key(s_over_threshold, 1)
    return sorted_list

def stations_highest_rel_level(stations, N):
    """returns a list of the N stations at which the water level, relative to the typical range, is highest"""
    #adds to a list stations with the 10 stations with the highest relative water level
    #skips stations with no data
    stationsWithHightWater = []
    for station in stations:
        if station.latest_level != None:
            if station.typical_range_consistent():
                stationsWithHightWater.append((station, station.relative_water_level()))
    #sorts the list by relative water level from largest to smallest
    sortedlist = sorted_by_key(stationsWithHightWater, 1, reverse = True)[:N]

    return sortedlist