from .utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples of stations with latest relative water levels over tol and their relative water levels"""
    
    s_over_threshold = []
    for station in stations:
        if station.typical_range_consistent:
            if station.relative_water_level() > tol:
                s_over_threshold.append((station, station.relative_water_level()))

    sorted_list = sorted_by_key(s_over_threshold, 1)
    return sorted_list
    