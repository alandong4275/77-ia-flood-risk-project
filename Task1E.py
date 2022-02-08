from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Requirements for Task 1E"""

    # Build list of stations
    stations = build_station_list()

    # Creates list of the 9 top rivers by station number
    rivers = rivers_by_station_number(stations, 9)

    # Displays list
    print("9 rivers with the most monitoring stations:")
    print(rivers)


if __name__ == "__main__":
    print("\n" + "*** Task 1E: CUED Part IA Flood Warning System ***" + "\n")
    run()

