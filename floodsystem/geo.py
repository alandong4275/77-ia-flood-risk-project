# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

def stations_by_distance(stations, p):
    '''returns a list of stations sorted by how far away they are from the point p'''
    #creating a list
    listStations = []

    #inserting in to the list the station names, towns, and distance away from a point p
    for i in stations:
        listStations.append((i, haversine(i.coord, p, unit=Unit.KILOMETERS)))

    #sorting the list by their distance away from a point p
    sortedList = sorted_by_key(listStations, 1)

    return sortedList

def stations_within_radius(stations, centre, r):
    '''returns a list of stations within a radius of a point, sorted alphabetically'''
    #creating a list
    stationsInRadius = []
    #finding the radius of each station from the centre
    for i in stations:
        radius = haversine(i.coord, centre, unit=Unit.KILOMETERS)
    #insterting the stations with radius smaller than r in to the list
        if radius < r:
            stationsInRadius.append(i)

    return stationsInRadius

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

def rivers_by_station_number(stations, N):
    """Returns a list of the N rivers with the greatest number of monitoring stations 
    and their number of monitoring stations"""

    # Creates a dictionary of rivers that map to their number of monitoring stations
    rivers = dict()
    for station in stations:
        # Increments number of monitoring stations by 1 for each new monitoring station by a given river
        if station.river is not None:
            if station.river in rivers.keys():
                rivers[station.river] += 1
            else:
                rivers[station.river] = 1
        else:
            pass

    # Converts dictionary into list of tuples
    river_list = [(key, value) for key, value in rivers.items()]

    # Sorts list by descending number of monitoring stations
    sorted_rivers = sorted_by_key(river_list, 1, reverse=True)

    # Truncates list to initial N items
    greatest_rivers = sorted_rivers[:N]

    return greatest_rivers
