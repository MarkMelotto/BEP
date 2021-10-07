import numpy as np
from functions import *

def WIKI_absorption_coefficient_air_composition_high_humidity(mu_H20):

    high_H2O = 0.03
    high_humidity = mu_H20 * high_H2O
    return high_humidity

def WIKI_find_humidity_from_intensity(start_intensity, received_intensity, path_length, mu_H2O):

    high_H2O = 0.03

    concentration_H2O = -((np.log(received_intensity / start_intensity)) / path_length) / mu_H2O

    percentage_humidity = (concentration_H2O / high_H2O) * 100

    return percentage_humidity


# now calculate absorption coefficient with the temperature
def WIKI_absorption_coefficient_air_composition_high_humidity_at_T(mu_H20, T):

    high_H2O = calculate_maximum_percentage_water(T)
    high_humidity = mu_H20 * high_H2O
    return high_humidity


def WIKI_find_humidity_from_intensity_at_T(start_intensity, received_intensity, path_length, mu_H2O, T):

    high_H2O = calculate_maximum_percentage_water(T)

    concentration_H2O = -((np.log(received_intensity / start_intensity)) / path_length) / mu_H2O

    percentage_humidity = (concentration_H2O / high_H2O) * 100

    return percentage_humidity

