import numpy as np
from functions import *
from functions.functions import *
'''functions for the HITRAN data base'''

# returns lowest and highest possible absorption coefficients for both air compositions
def HITRAN_absorption_coefficient_air_composition_low_high_humidity(mu_N2, mu_O2, mu_CO2, mu_H20):
    N2 = 0.78
    O2 = 0.209
    CO2 = 0.0003
    low_H2O = 0
    high_H2O = 0.03
    low_humidity = mu_CO2 * CO2 + mu_O2 * O2 + N2 * mu_N2 + mu_H20 * low_H2O
    high_humidity = mu_CO2 * CO2 + mu_O2 * O2 + N2 * mu_N2 + mu_H20 * high_H2O
    return low_humidity, high_humidity

def HITRAN_find_humidity_from_intensity(start_intensity, received_intensity, path_length, mu_N2, mu_O2, mu_CO2, mu_H2O):
    N2 = 0.78
    O2 = 0.209
    CO2 = 0.0003
    high_H2O = 0.03

    mu_known = mu_N2 * N2 + mu_CO2 * CO2 + mu_O2 * O2

    concentration_H2O = -(((np.log(received_intensity / start_intensity)) / path_length) + mu_known) / mu_H2O

    percentage_humidity = (concentration_H2O / high_H2O) * 100

    return percentage_humidity


# now calculate absorption coefficient with the temperature
def HITRAN_absorption_coefficient_air_composition_low_high_humidity_at_T(mu_N2, mu_O2, mu_CO2, mu_H20, T):
    N2 = 0.78
    O2 = 0.209
    CO2 = 0.0003
    low_H2O = 0
    high_H2O = calculate_maximum_percentage_water(T)
    low_humidity = mu_CO2 * CO2 + mu_O2 * O2 + N2 * mu_N2 + mu_H20 * low_H2O
    high_humidity = mu_CO2 * CO2 + mu_O2 * O2 + N2 * mu_N2 + mu_H20 * high_H2O
    return low_humidity, high_humidity


def HITRAN_find_humidity_from_intensity_at_T(start_intensity, received_intensity, path_length,
                                             mu_N2, mu_O2, mu_CO2, mu_H2O, T):
    N2 = 0.78
    O2 = 0.209
    CO2 = 0.0003
    high_H2O = calculate_maximum_percentage_water(T)

    mu_known = mu_N2 * N2 + mu_CO2 * CO2 + mu_O2 * O2

    concentration_H2O = -(((np.log(received_intensity / start_intensity)) / path_length) + mu_known) / mu_H2O

    percentage_humidity = (concentration_H2O / high_H2O) * 100

    return percentage_humidity