from functions.functions import *
import numpy as np

# all absorption coefficients are wavenumbers per cm: KNa per cm
mu_water = HITRAN_get_mu_water()

mu_nitrogen = HITRAN_get_mu_nitrogen()

mu_oxygen = HITRAN_get_mu_oxygen()

mu_carbon_mono_oxide = HITRAN_get_mu_carbon_mono_oxide()

# a list of wavenumbers to make it easier to look at all the data in the same loop
list_of_wavenumbers = [5344, 7210, 7400, 8812, 10638, 10700]

start_laser_intensity = 0.100  # Watt/cm2
path_length_laser = 10  # cm

for wavenumber in list_of_wavenumbers:

    T = np.random.randint(-20, 60) # outside temperature, degree Celsius
    current_wavelength = wavenumber_to_wavelength(wavenumber)
    REAL_humidity = np.random.randint(0,100) # %

    # getting the possible absorption coefficients of the air at this temperature T
    low_humidity, high_humidity = HITRAN_absorption_coefficient_air_composition_low_high_humidity_at_T(
        mu_nitrogen[wavenumber], mu_oxygen[wavenumber], mu_carbon_mono_oxide[wavenumber], mu_water[wavenumber], T)

    # converting the possible absorption coefficients into their respective intensities
    low_intensity = measure_intensity(start_laser_intensity, low_humidity, path_length_laser)
    high_intensity = measure_intensity(start_laser_intensity, high_humidity, path_length_laser)

    # from this we get our random 'measured' intensity
    random_intensity = ((high_intensity-low_intensity)*REAL_humidity/100) + low_intensity

    # from which we can calculate our way back to a percentage
    humidity = HITRAN_find_humidity_from_intensity_at_T(start_laser_intensity, random_intensity, path_length_laser,
                                                        mu_nitrogen[wavenumber], mu_oxygen[wavenumber],
                                                        mu_carbon_mono_oxide[wavenumber], mu_water[wavenumber], T
                                                        )

    print(f"\n"
          f"for wavelength: {current_wavelength * 1e9:.2f} nm at T = {T} Celsius:\n"
          f"The real humidity is: {REAL_humidity} %\n"
          f"Calculated humidity is: {humidity} %\n")