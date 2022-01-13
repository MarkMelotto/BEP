from functions.WIKI_functions import *
from functions.WIKI_data import *
from functions.functions import *

absorption_coefficient_water = WIKI_get_workable_absorption_coeff_water()
list_wavelengths = WIKI_workable_available_wavelengths()
wavelength = 940e-9

random_temperature = True
start_intensity = 0.100  # Watt/cm2
path_length = 0.2  # meter

# decimals rounded
decimal_round = 7

# number of iterations
N = 1000000
if not random_temperature:
    T = 10

error_list = []

for i in range(N):
    REAL_humidity = np.random.randint(0, 100)  # %
    if random_temperature:
        T = np.random.randint(-20, 60)

    concentration_water = WIKI_absorption_coefficient_air_composition_max_humidity_at_T(absorption_coefficient_water[wavelength], T)

    max_intensity_loss = measure_intensity(start_intensity, concentration_water, path_length)

    random_intensity = ((max_intensity_loss - start_intensity) * REAL_humidity / 100) + start_intensity

    # to make this work as a real life situation, we cannot measure at 10 decimals
    random_intensity = round(random_intensity, decimal_round)

    humidity = WIKI_find_humidity_from_intensity_at_T(start_intensity, random_intensity, path_length,
                                                 absorption_coefficient_water[wavelength], T)

    error_list.append(abs(humidity-REAL_humidity))
    # print(f"\n"
    #       f"for wavelength: {wavelength * 1e9:.2f} nm over a path length of {path_length * 100} cm at T = {T}:\n"
    #       f"The real humidity is: {REAL_humidity} %\n"
    #       f"Calculated humidity is: {humidity} %\n")


print(f"\nThe average error for {decimal_round} decimals W/cm2 with random temperature for wavelength {wavelength*1e9} nm is: \n"
      f"{sum(error_list)/len(error_list)} %")