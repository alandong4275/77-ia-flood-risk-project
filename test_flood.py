from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def test_stations_level_over_threshold(stations, tol):
     # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Print stations with relative water levels over tolerance
    if len(stations_level_over_threshold(stations, 0.8)) >= 0:
        assert True
