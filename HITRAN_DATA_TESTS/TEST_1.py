from functions.functions import *

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
    current_wavelength = wavenumber_to_wavelength(wavenumber)

    low_humidity_absorption_coefficient, high_humidity_absorption_coefficient = \
        HITRAN_absorption_coefficient_air_composition_low_high_humidity(mu_nitrogen[wavenumber], mu_oxygen[wavenumber],
                                                                        mu_carbon_mono_oxide[wavenumber], mu_water[wavenumber])

    absorbed_light_low_humidity_intensity = measure_intensity(start_laser_intensity,
                                                              low_humidity_absorption_coefficient, path_length_laser)
    absorbed_light_high_humidity_intensity = measure_intensity(start_laser_intensity,
                                                               high_humidity_absorption_coefficient, path_length_laser)

    intensity_low_dB = intensity_in_dB(start_laser_intensity, absorbed_light_low_humidity_intensity)
    intensity_high_dB = intensity_in_dB(start_laser_intensity, absorbed_light_high_humidity_intensity)

    print(f"\n"
          f"for wavelength: {current_wavelength * 1e9:.2f} nm:\n"
          f"low humidity: {absorbed_light_low_humidity_intensity:.4} Watt/cm2, {intensity_low_dB:.4} dB\n"
          f"high humidity: {absorbed_light_high_humidity_intensity:.4} Watt/cm2, {intensity_high_dB:.4} dB\n"
          f"a difference of: {((absorbed_light_high_humidity_intensity - absorbed_light_low_humidity_intensity) / absorbed_light_low_humidity_intensity) * 100:.4}% in intensity\n"
          f"and a change of: {intensity_low_dB - intensity_high_dB:.4} dB")
