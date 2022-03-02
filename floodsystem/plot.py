import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, date
import floodsystem.datafetcher as df
import floodsystem.analysis as anal
import numpy as np

def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the water level data and the best-fit polynomial"""
    #plots a polynomial of best fit for the data
    poly, d0 = anal.polyfit(dates, levels, p)
    #plots data
    x = matplotlib.dates.date2num(dates)
    y = levels
    plt.plot(dates, y)
    x1 = np.linspace(x[0], x[-1], len(dates))
    plt.plot(matplotlib.dates.num2date(x1), poly(x1 - d0))
    #adds red boundary lines for the low and high end of the typical range
    plt.axhline(y=station.typical_range[0], color='r', linestyle='-')
    plt.axhline(y=station.typical_range[1], color='r', linestyle='-')
    #adds labels and rotates the x labels by 45 degrees.
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(f"Station: {station.name}")

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_levels(station, dates, levels):
    """Plots water levels of station against time, with typical high, low values"""
    # Plot
    plt.plot(dates, levels)
    plt.axhline(y=station.typical_range[0], color='r', linestyle='-')
    plt.axhline(y=station.typical_range[1], color='r', linestyle='-')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(f"Station: {station.name}")

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
