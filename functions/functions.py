import numpy as np


'''some HITRAN data on the absorption coefficients on molecules all in 1/cm:'''
def HITRAN_get_mu_water():
    return {5344: 0.55, 7210: 0.4, 7400: 0.37, 8812: 0.03, 10700: 0.0129, 10638: 0.0006}

# def get_mu_nitrogen():
#     return {5344: -0.0275, 7210: -0.17, 7400: -0.14, 8812: -0.112, 10700: 0, 10638: 0}

def HITRAN_get_mu_nitrogen():
    return {5344: 0, 7210: 0, 7400: 0, 8812: 0, 10700: 0, 10638: 0}


def HITRAN_get_mu_oxygen():
    return {5344: 7.36E-6, 7210: 2.98E-5, 7400: 1.1E-5, 8812: 1.1E-5, 10700: 3.355E-5, 10638: 2.6E-5}


def HITRAN_get_mu_carbon_mono_oxide():
    return {5344: 0.0209, 7210: 3.36e-3, 7400: 3.11e-3, 8812: 2.490e-3, 10700: 3.86e-3, 10638: 4.11e-3}


'''DATA wikipedia in 1/m'''
def WIKI_get_absorption_coeff_water():
    return {718e-9:1, 810e-9:1.5, 1.13e-6:20, 1.38e-6:30, 1.88e-6:900, 2.68e-6:8000, 6.3e-6:15000}

'''basic functions'''
# function to measure the intensity left over after a certain path length
def measure_intensity(start_intensity, atten_coef, length):
    return start_intensity * np.exp(-atten_coef * length)

# returns the difference in dB between start signal and end signal
def intensity_in_dB(start_intensity, current_intensity):
    return 10 * np.log10(current_intensity / start_intensity)

def wavenumber_to_wavelength(WN):
    return 0.01 / (WN)

# returns water saturation at g/m3
def calculate_water_saturation(T):
    return np.exp(1.56065404) * np.exp(6.90219321e-02 * T) * np.exp(-2.38543241e-04 * T ** 2)

# returns air density at kg/m3
def calculate_air_density(T):
    return 1.44685243e-05 * T ** 2 - 4.72481940e-03 * T + 1.29255728


# returns decimal percentage of the max percentage water in the air at certain temperature T
# accurate between -20 and 60 C
def calculate_maximum_percentage_water(T):
    water_saturation = calculate_water_saturation(T)  # g/m3
    air_density = calculate_air_density(T)  # kg/m3

    max_percentage = (water_saturation / (air_density * 1000))  # decimal percentage

    return max_percentage

# returns lowest and highest possible absorption coefficients for both air compositions
def absorption_coefficient_air_composition_low_high_humidity(mu_N2, mu_O2, mu_CO2, mu_H20):
    N2 = 0.78
    O2 = 0.209
    CO2 = 0.0003
    low_H2O = 0
    high_H2O = 0.03
    low_humidity = mu_CO2 * CO2 + mu_O2 * O2 + N2 * mu_N2 + mu_H20 * low_H2O
    high_humidity = mu_CO2 * CO2 + mu_O2 * O2 + N2 * mu_N2 + mu_H20 * high_H2O
    return low_humidity, high_humidity


'''functions for the HITRAN data base'''
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


if __name__ == "__main__":
    print(f"testing the decimal percentage water in air: {calculate_maximum_percentage_water(20)}")
