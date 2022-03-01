from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2C"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    highest10 = (stations_highest_rel_level(stations, 10))

    for station in highest10:
        print(station[0].name, station[1])

if __name__ == "__main__":
    print("\n *** Task 2C: CUED Part IA Flood Warning System *** \n")
    run()
