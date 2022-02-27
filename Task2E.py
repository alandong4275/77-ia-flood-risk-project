from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
import datetime

def run():
    """Requirements for Task 2E"""

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    n_stations = stations_highest_rel_level(stations, 5)
    
    for station, r_level in n_stations:
        dt = 10
        dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days = dt))
        plot_water_levels(station, dates, levels)

if __name__ == "__main__":
    print("\n" + "*** Task 2E: CUED Part IA Flood Warning System ***" + "\n")
    run()
