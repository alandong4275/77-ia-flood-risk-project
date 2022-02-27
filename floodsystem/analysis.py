import numpy as np
import matplotlib as plt

def polyfit(dates, levels, p):
    """Returns a tuple of a least-squares fit polynomial object and any shift of the time (date) axis"""
    x = plt.dates.date2num(dates)
    print(x)
    y = levels
    p_coeff = np.polyfit(x - x[0], y, p)
    poly = np.poly1d(p_coeff)
    return (poly, -x[0])
