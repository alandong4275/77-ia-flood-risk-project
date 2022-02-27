import numpy as np
import matplotlib as mat

def polyfit(dates, levels, p):
    """Returns a tuple of a least-squares fit polynomial object and any shift of the time (date) axis"""
    x = mat.dates.date2num(dates)
    y = levels
    x0 = x[0]*len(x)
    p_coeff = np.polyfit(x - x[0], y, p)
    poly = np.poly1d(p_coeff)
    return (poly, x[0])
