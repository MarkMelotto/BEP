"""this py file tests the whole system and its variables"""

from functions.WIKI_functions import *
from functions.WIKI_data import *
from functions.functions import *

# system variables

laser_power = 2  # mWatt

diameter_laser = 10  # mm

laser_path_length = 0.2  # m

resistance_resistor = 1000  # Ohm

relative_spectral_sensitivity = 0.95  # 980nm
# relative_spectral_sensitivity = 1  # 940nm

# angle_laser_beam_on_detector = 0 # degree

# reverse_voltage = 5


# |---- data ----|

absorption_coefficient_water = WIKI_get_workable_absorption_coeff_water()

wavelength = 980e-9

temperature = 20  # C

humidity = 70  # %

# |---- calculations ----|

surface_area_laser = np.pi * (diameter_laser / 2) ** 2  # mm2
surface_area_detector = 6.5  # mm2
intensity_at_laser_tip = laser_power / surface_area_laser  # mWatt/mm2
intensity_at_laser_tip *= 100  # mWatt/cm2

# |---- humidity calculations ----|

max_attenuation = WIKI_absorption_coefficient_air_composition_max_humidity_at_T(absorption_coefficient_water[wavelength], temperature)
attenuation = (humidity/100) * max_attenuation

light_at_detector = measure_intensity(intensity_at_laser_tip, attenuation, laser_path_length)

# |---- calculating the current this induces ----|

induced_current = photodetector_1(light_at_detector)*relative_spectral_sensitivity

voltage_measured = resistance_resistor * induced_current

print(f"Wavelength: {wavelength*1e9:.0f} nm, T = {temperature} C, humidity = {humidity} %, \n"
      f"distance = {laser_path_length*100:.0f} cm, resistance = {resistance_resistor} Ohm\n"
      f"laser power = {laser_power} mWatt, pulse diameter = {diameter_laser} mm \n"
      f"\n"
      f"laser intensity to start with: {intensity_at_laser_tip:.3f} mW/cm2\n"
      f"laser intensity at detector: {light_at_detector:.3f} mW/cm2\n"
      f"this gives a current of: {induced_current*1e6:.2f} uA\n"
      f"which gives us a voltage of: {voltage_measured*1e3:.2f} mV")