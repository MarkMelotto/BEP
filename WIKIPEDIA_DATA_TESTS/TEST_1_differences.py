from functions.functions import *

absorption_coefficient_water = WIKI_get_absorption_coeff_water()
list_wavelengths = WIKI_available_wavelengths()

start_intensity = 0.100  # Watt/cm2
path_length = 0.1 # meter

for wavelength in list_wavelengths:




    print(f"\n"
          f"for wavelength: {wavelength * 1e9:.2f} nm:\n"
          f"low humidity: {absorbed_light_low_humidity_intensity:.4} Watt/cm2, {intensity_low_dB:.4} dB\n"
          f"high humidity: {absorbed_light_high_humidity_intensity:.4} Watt/cm2, {intensity_high_dB:.4} dB\n"
          f"a difference of: {((absorbed_light_high_humidity_intensity - absorbed_light_low_humidity_intensity) / absorbed_light_low_humidity_intensity) * 100:.4}% in intensity\n"
          f"and a change of: {intensity_low_dB - intensity_high_dB:.4} dB")