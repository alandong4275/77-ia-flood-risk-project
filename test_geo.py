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

