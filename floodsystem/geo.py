# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def rivers_with_station(stations):
    """Returns a list of the names of rivers with a monitoring station"""

    # Creates a set of rivers with monitoring stations
    rivers = set()
    for station in stations:
        if station.river is not None:
            rivers.add(station.river)

    # Converts set into alphabetically ordered list
    sorted_rivers = sorted(rivers)

    return sorted_rivers

def stations_by_river(stations):
    """Returns a dictionary mapping the names of rivers with a list of their monitoring station"""

    # Creates a dictionary of rivers that map to a list of their monitoring stations
    rivers = dict()
    for station in stations:
        # Adds names of monitoring stations into the list under each river
        if station.river is not None:
            if station.river in rivers.keys():
                rivers[station.river].append(station.name)
            else:
                rivers[station.river] = [station.name]
        else:
            pass

    # Sorts the lists of monitoring stations alphabetically
    for river in rivers.keys():
        rivers[river].sort()

    return rivers
