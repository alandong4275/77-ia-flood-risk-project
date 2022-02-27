from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    """Requirements for Task 2G"""

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    low_risk = []
    moderate_risk = []
    high_risk = []
    severe_risk = []

    for station in stations:
        if station.latest_level != None:
            if station.typical_range_consistent():
                if station.relative_water_level() <= 1:
                    low_risk.append(station)
                elif station.relative_water_level() <= 3:
                    moderate_risk.append(station)
                elif station.relative_water_level() <= 4:
                    high_risk.append(station)
                else:
                    severe_risk.append(station)

    print(f"Low risk stations: {len(low_risk)}")
    print(f"Moderate risk stations: {len(moderate_risk)}")
    print(f"High risk stations: {len(high_risk)}")
    print(f"Severe risk stations: {len(severe_risk)}")

if __name__ == "__main__":
    print("\n" + "*** Task 2G: CUED Part IA Flood Warning System ***" + "\n")
    run()