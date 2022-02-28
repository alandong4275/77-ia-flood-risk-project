import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, date
import floodsystem.datafetcher as df
import floodsystem.analysis as anal
import numpy as np

def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the water level data and the best-fit polynomial"""
    poly, d0 = anal.polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)
    y = levels
<<<<<<< HEAD
    plt.plot(x - d0, y, '.')
    x1 = np.linspace(0, x[-1] - d0, 30)
    plt.plot(x1, poly(x1))
    plt.xlabel = station.measure_id
    plt.show()
=======
    plt.plot(dates, y)
    x1 = np.linspace(x[0], x[-1], len(dates))
    plt.plot(matplotlib.dates.num2date(x1), poly(x1 - d0))

    plt.axhline(y=station.typical_range[0], color='r', linestyle='-')
    plt.axhline(y=station.typical_range[1], color='r', linestyle='-')

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
>>>>>>> 4fdde51f03e58997a9e9bb4df16e7099b00faa37
