from functions.WIKI_functions import *
from functions.WIKI_data import *
from functions.functions import *

absorption_coefficient_water = WIKI_get_absorption_coeff_water()
list_wavelengths = WIKI_available_wavelengths()

start_intensity = 0.100  # Watt/cm2
path_length = 0.1  # meter
T = 20

for wavelength in list_wavelengths:
    low_humidity_absorption_coefficient, high_humidity_absorption_coefficient = \
        0, WIKI_absorption_coefficient_air_composition_high_humidity_at_T(absorption_coefficient_water[wavelength], T)

    absorbed_light_low_humidity_intensity = measure_intensity(start_intensity,
                                                              low_humidity_absorption_coefficient, path_length)
    absorbed_light_high_humidity_intensity = measure_intensity(start_intensity,
                                                               high_humidity_absorption_coefficient,
                                                               path_length)

    intensity_low_dB, intensity_high_dB = intensity_in_dB(start_intensity, absorbed_light_low_humidity_intensity), \
                                          intensity_in_dB(start_intensity, absorbed_light_high_humidity_intensity)

    print(f"\n"
          f"for wavelength: {wavelength * 1e9:.2f} nm over a path length of {path_length * 100} cm at T = {T}:\n"
          f"no water vapor: {absorbed_light_low_humidity_intensity} Watt/cm2, {intensity_low_dB:.4} dB\n"
          f"highest possible water vapor: {absorbed_light_high_humidity_intensity} Watt/cm2, {intensity_high_dB:.4} dB\n"
          f"a difference of: {((absorbed_light_high_humidity_intensity - absorbed_light_low_humidity_intensity) / absorbed_light_low_humidity_intensity) * 100:.4}% in intensity\n"
          f"and a change of: {intensity_low_dB - intensity_high_dB:.4} dB")