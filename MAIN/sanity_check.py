from functions.WIKI_functions import *
from functions.WIKI_data import *
from functions.functions import *
import matplotlib.pyplot as plt

absorption_coefficient_water = WIKI_get_workable_absorption_coeff_water()

wavelength = 980e-9
temperature = 20

max_attenuation = WIKI_absorption_coefficient_air_composition_max_humidity_at_T(
                    absorption_coefficient_water[wavelength], temperature)

attenuation = (50 / 100) * max_attenuation  # dit is mu*c

light_at_detector = measure_intensity(1.7, attenuation, 0.4)
induced_current = photodetector_1(light_at_detector) * 0.95
volt = induced_current * 46.5e3

max_c = calculate_maximum_percentage_water(temperature)  # c

print(attenuation/absorption_coefficient_water[wavelength])
print(max_c)
print(f"percentage = {((attenuation/absorption_coefficient_water[wavelength])/max_c) * 100}")
print(f"volt = {volt*1e3}")