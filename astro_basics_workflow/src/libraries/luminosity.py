# src/libraries/luminosity.py
import numpy as np

def luminosity_function(l, a, b, l_cen, A, alpha, beta):
    l_star = a * l_cen + b
    power_law_1 = (l / l_star) ** alpha
    power_law_2 = np.exp(-(l / l_star)**beta)
    num_sat = A * power_law_1 * power_law_2

    return num_sat
