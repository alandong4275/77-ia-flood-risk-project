from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.utils import sorted_by_key

def run():
    #Build list of stations
    stations = build_station_list()
    #adding the conditions
    coordinate = (52.2053, 0.1218)
    radius = 10
    #using function in geo
    listOfStationsInRadius = [station.name for station in stations_within_radius(stations, coordinate, radius)]
    sortedStations = sorted_by_key(listOfStationsInRadius, 0)

    print("Stations within a 10km radius of the city centre")
    print(sortedStations)


if __name__ == "__main__":
       print("*** Task 1B: CUED Part IA Flood Warning System ***")
       run()


