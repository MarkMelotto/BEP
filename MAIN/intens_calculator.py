from functions.WIKI_functions import *
from functions.WIKI_data import *
from functions.functions import *

absorption_coefficient_water = WIKI_get_workable_absorption_coeff_water()

wavelength = 980e-9
temperature = 20

max_attenuation = WIKI_absorption_coefficient_air_composition_max_humidity_at_T(
                    absorption_coefficient_water[wavelength], temperature)

attenuation = (500 / 100) * max_attenuation  # dit is mu*c

max_c = calculate_maximum_percentage_water(temperature)  # c
path_length = 0.4

R = 46.5e3
# spectral_sensitivity = 0.9
spectral_sensitivity = input("what is the current spectral sensitivity?:\n")
spectral_sensitivity = float(spectral_sensitivity)

while True:
    volt = input("\ngimme the voltage measured in mV\n")
    volt = float(volt)  # mVolt
    volt *= 1e-3  # Volt
    current = volt/R  # Ampere
    current *= 1e6  # uA
    intensity = (current / 37) / spectral_sensitivity

    print(f"incoming intensity = {intensity} mW/cm2\n")

    c_h20 = (np.log(1.7)-np.log(intensity))/(absorption_coefficient_water[wavelength] * path_length)

    print(attenuation / absorption_coefficient_water[wavelength])
    print(attenuation)
    print(c_h20 / absorption_coefficient_water[wavelength])
    print(max_c)
    print(f"percentage = {((c_h20) / max_c) * 100}")