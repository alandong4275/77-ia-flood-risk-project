from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    """Requirements for Task 2B"""

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Print stations with relative water levels over tolerance
    for station_tuple in stations_level_over_threshold(stations, 0.8):
        print(station_tuple[0] + " " + station_tuple[0].relative_water_level())

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
