"""this py file tests the whole system and its variables"""
import numpy as np

from functions.WIKI_functions import *
from functions.WIKI_data import *
from functions.functions import *
import matplotlib.pyplot as plt

# system variables

laser_power = [3]  # mWatt

diameter_laser = [15]  # mm

laser_path_length = np.arange(0.1, .5, .1)  # m

resistance_resistor = [1e3, 1e4, 1e5]  # Ohm

relative_spectral_sensitivity = 0.95  # 980nm
# relative_spectral_sensitivity = 1  # 940nm

# angle_laser_beam_on_detector = 0 # degree

reverse_voltage = 5


# |---- data ----|

absorption_coefficient_water = WIKI_get_workable_absorption_coeff_water()

wavelength = 980e-9

temperature = 20  # C

humidity = np.linspace(1, 100)  # %

# |---- empty list for plots ----|

y = np.zeros((len(laser_path_length), len(humidity), len(resistance_resistor)))
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

                light_at_detector_low = measure_intensity(intensity_at_laser_tip, attenuation_low, laser_path_length[i])

                # |---- calculating the current this induces ----|

                induced_current_low = photodetector_1(light_at_detector_low) * relative_spectral_sensitivity

                # the plot data
                y[i, hum, :] = induced_current_low

# starting plot
resistor_measurement = y

for i in range(len(resistance_resistor)):
    resistor_measurement[:,:,i] *= resistance_resistor[i]


voltage_measured = resistor_measurement  # this is sloppy, i know

for i in range(len(voltage_measured[:,0,0])):
    for j in range(len(voltage_measured[0,:,0])):
        for k in range(len(voltage_measured[0,0,:])):

            if voltage_measured[i, j, k] > reverse_voltage:
                voltage_measured[i, j, k] = reverse_voltage

voltage_measured *= 1e3  # to make it into mV
# y *= 1e6

fig, axs = plt.subplots(4, 3, figsize=(20,15))


for i in range(4):
    for j in range(3):
        axs[i,j].plot(humidity, voltage_measured[i, :, j])
        axs[i,j].set_title(f"measured voltage, I = {intensity[0]:.2f} mW/cm2, path = {laser_path_length[i]*100:.1f} cm\n"
                           f"resistance = {resistance_resistor[j]:.0f} Ohm")
        axs[i,j].grid()
        axs[i,j].set_xlabel(f'light ({wavelength * 1e9:.0f} nm) humidity (%)')
        axs[i,j].set_ylabel('mV')

plt.tight_layout()
plt.show()
