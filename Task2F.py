from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
import datetime

def run():
    """Requirements for Task 2F"""

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    n_stations = stations_highest_rel_level(stations, 5)
    
    for station, r_level in n_stations:
        dt = 2
        dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days = dt))
        if dates != []:
            plot_water_level_with_fit(station, dates, levels, 4)

if __name__ == "__main__":
    print("\n" + "*** Task 2F: CUED Part IA Flood Warning System ***" + "\n")
    run()
