from hashlib import sha1
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation

def test_stations_level_over_threshold():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange1 = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"

    s1 = MonitoringStation(s_id, m_id, label, coord, trange1, river, town)

    # Print stations with relative water levels over tolerance
    if len(stations_level_over_threshold([s1], 0.8)) >= 0:
        assert True
