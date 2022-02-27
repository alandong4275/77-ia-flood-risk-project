from floodsystem.stationdata import build_station_list, update_water_levels
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
    run()
