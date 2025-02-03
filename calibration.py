
""" 
This module contains calibration functions for Vasicek and Ho-Lee models.
"""
import numpy as np
from scipy.optimize import least_squares

def vasicek_calibration(params, r, dt):
    a, b, sigma = params
    r_lag, r_next = r[:-1], r[1:]
    expected_change = a * (b - r_lag) * dt
    residuals = (r_next - r_lag - expected_change) / (sigma + 1e-6)
    return residuals

def calibrate_vasicek(rate_data, dt):
    initial_params = [0.1, np.mean(rate_data), 0.01]
    result = least_squares(vasicek_calibration, initial_params, args=(rate_data, dt))
    return result.x

def holee_calibration(params, r, dt):
    theta, sigma = params
    r_lag, r_next = r[:-1], r[1:]
    expected_change = theta * dt
    residuals = (r_next - r_lag - expected_change) / (sigma + 1e-6)
    return residuals

def calibrate_holee(rate_data, dt):
    initial_params = [0.001, 0.01]
    result = least_squares(holee_calibration, initial_params, args=(rate_data, dt))
    return result.x
