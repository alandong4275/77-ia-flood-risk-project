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
