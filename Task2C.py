from floodsystem.stationdata import build_station_list, update_water_levels
<<<<<<< HEAD
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2B"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    highest10 = (stations_highest_rel_level(stations, 10))

    for station in highest10:
        print(station[0].name, station[1])

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
=======
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2C"""

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Print stations with relative water levels over tolerance
    for station_tuple in stations_highest_rel_level(stations, 10):
        print(station_tuple[0].name + " " + str(station_tuple[1]))

if __name__ == "__main__":
    print("\n" + "*** Task 2C: CUED Part IA Flood Warning System ***" + "\n")
>>>>>>> 4fdde51f03e58997a9e9bb4df16e7099b00faa37
    run()
