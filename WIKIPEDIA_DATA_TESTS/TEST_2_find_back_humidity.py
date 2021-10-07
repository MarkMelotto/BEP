from functions.WIKI_functions import *
from functions.WIKI_data import *
from functions.functions import *
import matplotlib.pyplot as plt

absorption_coefficient_water = WIKI_get_absorption_coeff_water()
dict_wavelengths = {718e-9:0.0997004495503373,
                    810e-9:0.09955101098295706,
                    940e-9:0.09417645335842488,
                    1.15e-6:0.0740818220681718,
                    1.38e-6:0.09139311852712283,
                    1.88e-6:0.006720551273974976,
                    2.68e-6:3.775134544279098e-12,
                    6.3e-6:2.8625185805493938e-21
                    }

start_intensity = 0.100  # Watt/cm2
path_length = 0.1  # meter

# lists for the plot
list_real_humidity = []
list_calculated_humidity = []
list_wavelengths = WIKI_available_wavelengths()

for wavelength, max_intensity_loss in dict_wavelengths.items():
    REAL_humidity = np.random.randint(0, 100)  # %

    list_real_humidity.append(REAL_humidity) # for a plot

    random_intensity = ((max_intensity_loss - start_intensity) * REAL_humidity / 100) + start_intensity

    humidity = WIKI_find_humidity_from_intensity(start_intensity, random_intensity, path_length,
                                                 absorption_coefficient_water[wavelength])

    list_calculated_humidity.append(humidity) # for a plot

    print(f"\n"
          f"for wavelength: {wavelength * 1e9:.2f} nm over a path length of {path_length * 100} cm:\n"
          f"The real humidity is: {REAL_humidity} %\n"
          f"Calculated humidity is: {humidity} %\n")


plt.plot(list_wavelengths, list_real_humidity, 'go', label='Real humidity')
plt.plot(list_wavelengths, list_calculated_humidity, 'r.', label='Calculated humidity')
plt.legend()
plt.grid()
plt.xlabel('Wavelength (m)')
plt.ylabel('Percentage Humidity')
plt.show()