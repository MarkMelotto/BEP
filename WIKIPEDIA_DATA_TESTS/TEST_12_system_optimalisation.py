"""this py file tests the whole system and its variables"""

from functions.WIKI_functions import *
from functions.WIKI_data import *
from functions.functions import *

# system variables

laser_power = np.linspace(1, 3)  # mWatt

diameter_laser = np.linspace(5, 15)  # mm

laser_path_length = np.arange(0.1,.45,.05)  # m

resistance_resistor = 1000  # Ohm

relative_spectral_sensitivity = 0.95  # 980nm
# relative_spectral_sensitivity = 1  # 940nm

# angle_laser_beam_on_detector = 0 # degree

# reverse_voltage = 5


# |---- data ----|

absorption_coefficient_water = WIKI_get_workable_absorption_coeff_water()

wavelength = 980e-9

temperature = 20  # C

humidity = [50, 51]  # %

# |----set of best parameters ----|

best_laser_power = 0
best_diameter_laser = 0
best_laser_path_length = 0
best_intensity_at_laser_tip = 0
best_light_at_detector = 0
best_induced_current_low = 0
best_induced_current_high = 0
best_voltage_low = 0
best_voltage_high = 0
best_difference = 0

# |---- calculations ----|

for power in laser_power:
    for diameter in diameter_laser:
        surface_area_laser = np.pi * (diameter / 2) ** 2  # mm2
        surface_area_detector = 6.5  # mm2
        intensity_at_laser_tip = power / surface_area_laser  # mWatt/mm2
        intensity_at_laser_tip *= 100  # mWatt/cm2

        # |---- humidity calculations ----|
        for path in laser_path_length:

            max_attenuation = WIKI_absorption_coefficient_air_composition_max_humidity_at_T(
                absorption_coefficient_water[wavelength], temperature)
            attenuation_low = (humidity[0] / 100) * max_attenuation
            attenuation_high = (humidity[1] / 100) * max_attenuation

            light_at_detector_low = measure_intensity(intensity_at_laser_tip, attenuation_low, path)
            light_at_detector_high = measure_intensity(intensity_at_laser_tip, attenuation_high, path)

            # |---- calculating the current this induces ----|

            induced_current_low = photodetector_1(light_at_detector_low)*relative_spectral_sensitivity
            induced_current_high = photodetector_1(light_at_detector_high)*relative_spectral_sensitivity

            difference = abs(induced_current_low-induced_current_high)

            voltage_measured_low = resistance_resistor * induced_current_low
            voltage_measured_high = resistance_resistor * induced_current_high

            if difference > best_difference:
                best_difference = difference
                best_laser_power = power
                best_diameter_laser = diameter
                best_laser_path_length = path
                best_intensity_at_laser_tip = intensity_at_laser_tip
                best_light_at_detector = light_at_detector_low
                best_induced_current_low = induced_current_low
                best_induced_current_high = induced_current_high
                best_voltage_low = voltage_measured_low
                best_voltage_high = voltage_measured_high

print(f"max found difference between lowest humidity found at:\n"
      f"Wavelength: {wavelength * 1e9:.0f} nm, T = {temperature} C, humidity = {humidity[0]}-{humidity[1]} % \n"
      f"distance = {best_laser_path_length * 100:.0f} cm, resistance = {resistance_resistor} Ohm\n"
      f"laser power = {best_laser_power} mWatt, pulse diameter = {best_diameter_laser} mm \n"
      f"\n"
      f"the best difference = {best_difference * 1e6:.2f} uA\n"
      f"\n"
      f"laser intensity to start with: {best_intensity_at_laser_tip:.3f} mW/cm2\n"
      f"laser intensity at detector: {best_light_at_detector:.3f} mW/cm2\n"
      f"this gives a current of: {best_induced_current_low * 1e6:.2f}-{best_induced_current_high * 1e6:.2f} uA\n"
      f"which gives a voltage of: {best_voltage_low * 1e3:.2f}-{best_voltage_high * 1e3:.2f} mV")
