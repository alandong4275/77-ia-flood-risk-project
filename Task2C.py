from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2C"""

    # Build list of stations
    stations = build_station_list()
    # Update the lateset level data for all stations
    update_water_levels(stations)
    # Using the function from flood to create a list with the 10 stations with the highest relative water level
    highest10 = (stations_highest_rel_level(stations, 10))
    # printing the name of the station and the relative water level for each object in "highest10"
    for station in highest10:
        print(station[0].name, station[1])

if __name__ == "__main__":
    print("\n *** Task 2C: CUED Part IA Flood Warning System *** \n")
    run()
