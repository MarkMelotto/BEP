from functions.functions import *
import numpy as np

# all absorption coefficients are wavenumbers per cm: KNa per cm
mu_water = get_mu_water()

mu_nitrogen = get_mu_nitrogen()

mu_oxygen = get_mu_oxygen()

mu_carbon_mono_oxide = get_mu_carbon_mono_oxide()

# a dict of wavenumbers to make it easier to look at all the data in the same loop plus the lowest and highest intensity
dict_of_wavenumbers = {5344:[0.09999219206483513, 0.08478275010972336],
                       7210:[0.09999276406180664, 0.08868562597025324],
                       7400:[0.09999676805222857, 0.08949098249760792],
                       8812:[0.09999695404639011, 0.0991010192142691],
                       10638:[0.09999333322223952, 0.09997533604205432],
                       10700:[0.09999183038373133, 0.09960560981897121]
                       }

start_laser_intensity = 0.100  # Watt/cm2
path_length_laser = 10  # cm

for wavenumber,intensity in dict_of_wavenumbers.items():
    current_wavelength = wavenumber_to_wavelength(wavenumber)
    REAL_humidity = np.random.randint(0,100) # %

    low_intensity, high_intensity = intensity

    random_intensity = ((high_intensity-low_intensity)*REAL_humidity/100) + low_intensity

    humidity = find_humidity_from_intensity(start_laser_intensity, random_intensity, path_length_laser,
                                            mu_nitrogen[wavenumber], mu_oxygen[wavenumber],
                                            mu_carbon_mono_oxide[wavenumber], mu_water[wavenumber]
                                            )

    print(f"\n"
          f"for wavelength: {current_wavelength * 1e9:.2f} nm:\n"
          f"The real humidity is: {REAL_humidity} %\n"
          f"Calculated humidity is: {humidity} %\n")
