import matplotlib.pyplot as plt
from datetime import datetime, timedelta, date
import floodsystem.datafetcher as df
import floodsystem.analysis as anal
import numpy as np

def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the water level data and the best-fit polynomial"""
    poly, d0 = anal.polyfit(dates, levels, p)
    x = plt.dates.date2num(dates)
    y = levels
    plt.plot(x - d0, y, '.')
    x1 = np.linspace(0, x[-1] - d0, 30)
    plt.plot(x1, poly(x1))
    plt.xlabel = station.measure_id
    plt.show()