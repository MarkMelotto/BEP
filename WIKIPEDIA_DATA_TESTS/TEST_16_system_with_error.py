"""this py file tests the whole system and its variables"""

from functions.WIKI_functions import *
from functions.WIKI_data import *
from functions.functions import *
import matplotlib.pyplot as plt

# system variables

laser_power = [3]  # mWatt

diameter_laser = [15]  # mm

laser_path_length = np.arange(0.1, .5, .1)  # m

resistance_resistor = [1e3, 1e4, 5e4]  # Ohm

relative_spectral_sensitivity = 0.95  # 980nm
# relative_spectral_sensitivity = 1  # 940nm

# angle_laser_beam_on_detector = 0 # degree

reverse_voltage = 5

resistor_error = 0.001

path_length_error = 0.005  # m = .5 cm

# |---- data ----|

absorption_coefficient_water = WIKI_get_workable_absorption_coeff_water()

wavelength = 980e-9

temperature = 20  # C

humidity = np.linspace(1, 100)  # %

# |---- empty list for plots ----|

y = np.zeros((len(laser_path_length), len(humidity), len(resistance_resistor)))
error_low = y.copy()
error_high = y.copy()
error_difference = y.copy()
intensity = []


# |---- calculations ----|

for power in laser_power:
    for diameter in range(len(diameter_laser)):
        surface_area_laser = np.pi * (diameter_laser[diameter] / 2) ** 2  # mm2
        surface_area_detector = 6.5  # mm2
        intensity_at_laser_tip = power / surface_area_laser  # mWatt/mm2
        intensity_at_laser_tip *= 100  # mWatt/cm2
        intensity.append(intensity_at_laser_tip)

        for hum in range(len(humidity)):
            # |---- humidity calculations ----|
            for i in range(len(laser_path_length)):
                max_attenuation = WIKI_absorption_coefficient_air_composition_max_humidity_at_T(
                    absorption_coefficient_water[wavelength], temperature)
                attenuation_low = (humidity[hum] / 100) * max_attenuation

                light_at_detector = measure_intensity(intensity_at_laser_tip, attenuation_low, laser_path_length[i])

                light_at_detector_low_error = measure_intensity(intensity_at_laser_tip, attenuation_low, laser_path_length[i] - path_length_error)
                light_at_detector_high_error = measure_intensity(intensity_at_laser_tip, attenuation_low, laser_path_length[i] + path_length_error)

                # |---- calculating the current this induces ----|

                induced_current = photodetector_1(light_at_detector) * relative_spectral_sensitivity

                induced_current_low_error = photodetector_1(light_at_detector_low_error) * relative_spectral_sensitivity
                induced_current_high_error = photodetector_1(light_at_detector_high_error) * relative_spectral_sensitivity

                # the plot data
                y[i, hum, :] = induced_current
                error_low[i, hum, :] = induced_current_low_error
                error_high[i, hum, :] = induced_current_high_error

# more calculations
resistor_measurement = y.copy()
# error_low = y.copy()
# error_high = y.copy()
# error_difference = y.copy()

for i in range(len(resistance_resistor)):
    resistor_measurement[:, :, i] *= resistance_resistor[i]


voltage_measured = resistor_measurement  # this is sloppy, i know

# check if the voltage exceeds reverse voltage
for i in range(len(voltage_measured[:, 0, 0])):
    for j in range(len(voltage_measured[0, :, 0])):
        for k in range(len(voltage_measured[0, 0, :])):

            if voltage_measured[i, j, k] > reverse_voltage:
                voltage_measured[i, j, k] = reverse_voltage

for i in range(len(resistance_resistor)):
    low_point = (resistance_resistor[i] - (resistance_resistor[i] * resistor_error))
    high_point = (resistance_resistor[i] + (resistance_resistor[i] * resistor_error))
    error_low[:, :, i] *= low_point
    error_high[:, :, i] *= high_point
    error_difference[:, :, i] = abs(error_high[:, :, i] - error_low[:, :, i])

# check if the voltage exceeds reverse voltage
for i in range(len(voltage_measured[:, 0, 0])):
    for j in range(len(voltage_measured[0, :, 0])):
        for k in range(len(voltage_measured[0, 0, :])):

            if error_low[i, j, k] > reverse_voltage:
                error_low[i, j, k] = reverse_voltage
            if error_high[i, j, k] > reverse_voltage:
                error_high[i, j, k] = reverse_voltage

for i in range(len(resistance_resistor)):
    error_difference[:, :, i] = abs(error_high[:, :, i] - error_low[:, :, i])

voltage_measured *= 1e3  # to make it into mV
error_low *= 1e3
error_high *= 1e3
error_difference *= 1e3 / 2
# y *= 1e6

# lets look at the difference

differences = np.zeros(voltage_measured.shape)

for i in range(len(voltage_measured[:, 0, 0])):
    for j in range(len(voltage_measured[0, :, 0])-1):
        for k in range(len(voltage_measured[0, 0, :])):
            differences[i, j, k] = abs(voltage_measured[i, j, k] - voltage_measured[i, j+1, k])

# plot

fig, axs = plt.subplots(len(laser_path_length), len(resistance_resistor), figsize=(20, 15))

for i in range(len(laser_path_length)):
    for j in range(len(resistance_resistor)):
        axs[i, j].errorbar(humidity, voltage_measured[i, :, j], yerr=error_difference[i, :, j],
                           fmt='-o', label='calculated potential + error')
        # axs[i, j].plot(humidity, voltage_measured[i, :, j], label='calculated potential')
        # axs[i, j].plot(humidity, error_low[i, :, j], label='min error')
        # axs[i, j].plot(humidity, error_high[i, :, j], label='max error')
        axs[i, j].set_title(
            f"difference voltage, I = {intensity[0]:.2f} mW/cm2, path = {laser_path_length[i] * 100:.1f} cm\n"
            f"resistance = {resistance_resistor[j]:.0f} Ohm, Vr = {reverse_voltage} V \n"
            f"error in R = {resistor_error*100:.1f} %, error in path length = {path_length_error*100:.1f} cm")
        axs[i, j].grid()
        axs[i, j].set_xlabel(f'light ({wavelength * 1e9:.0f} nm) humidity (%)')
        axs[i, j].set_ylabel('mV')
        axs[i, j].legend()


plt.tight_layout()
plt.show()
