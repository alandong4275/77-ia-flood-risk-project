from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    # Creates list of rivers with stations
    rivers = rivers_with_station(stations)
    no_of_rivers = len(rivers)

    # Displays list
    print("Rivers with at least one monitoring station:")
    print(f"{no_of_rivers} rivers. First 10 - {rivers[:10]}\n")

    # Creates dictionary of rivers mapping to their monitoring stations
    s_by_rivers = stations_by_river(stations)

    # Displays lists of monitoring stations by the rivers Aire, Cam and Thames
    print(f"Monitoring stations by the River Aire:")
    print(s_by_rivers["River Aire"])
    print("\n")

    print(f"Monitoring stations by the River Cam:")
    print(s_by_rivers["River Cam"])
    print("\n")

    print(f"Monitoring stations by the River Thames:")
    print(s_by_rivers["River Thames"])


if __name__ == "__main__":
    print("\n" + "*** Task 1D: CUED Part IA Flood Warning System ***" + "\n")
    run()

