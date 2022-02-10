from sqlalchemy import true
from floodsystem.station import MonitoringStation
from floodsystem import geo
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit

from floodsystem.utils import sorted_by_key

def test_stations_by_distance():
    # Build list of stations
    stations = build_station_list()
    p = (-2.0, 4.0)

    sorted_stations = geo.stations_by_distance(stations, p)

    for index in range(0, len(sorted_stations)):
        assert haversine(sorted_stations[index].coord, p, unit=Unit.KILOMETERS) < haversine(sorted_stations[index+1].coord, p, unit=Unit.KILOMETERS)


def test_stations_within_radius():
    # Build list of stations
    stations = build_station_list()
    r = 10
    centre = (52.2053, 0.1218)
    s_w_r = geo.stations_within_radius(stations, centre, r)

    for index in range(0, len(s_w_r)):
        assert haversine(s_w_r[index], centre) < 10

def test_rivers_with_station():
    # Build list of stations
    stations = build_station_list()
    no_of_rivers = 0

    for station in stations:
        if station.river is not None:
            no_of_rivers += 1

    assert len(geo.rivers_with_station(stations)) == no_of_rivers

def test_stations_by_river():
    # Build list of stations
    stations = build_station_list()

    rivers = geo.stations_by_river(stations)
    for r in rivers.keys():
        for s in rivers[r]:
            for station in stations:
                if station.name == s:
                    assert station.river == r

def test_rivers_by_station_number():
    # Build list of stations
    stations = build_station_list()

    greatest_r = geo.rivers_by_station_number(stations, 10)

    assert len(greatest_r) == 10
    for i in range(0, greatest_r):
        assert greatest_r[i][1] > greatest_r[i+1][1]