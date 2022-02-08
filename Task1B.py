from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    #Build list of stations
    stations = build_station_list()
    #Centre P
    coordinate = (52.2053, 0.1218)
    #Using the function in geo to get a list of stations by distance using the centre P
    listOfStationsByDistance = stations_by_distance(stations, coordinate)

    closest_stations = [(station.name, station.town, distance) for (station, distance) in listOfStationsByDistance[:10]]
    furthest_stations = [(station.name, station.town, distance) for (station, distance) in listOfStationsByDistance[-10:]]

    print("10 closest stations")
    print(closest_stations)

    print("10 furthest stations")
    print(furthest_stations)



if __name__ == "__main__":
       print("*** Task 1B: CUED Part IA Flood Warning System ***")
       run()
