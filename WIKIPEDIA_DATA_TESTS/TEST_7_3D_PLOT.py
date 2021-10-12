from functions.WIKI_functions import *
from functions.WIKI_data import *
from functions.functions import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


wavelength = 940e-9

absorption_coefficient_water = WIKI_get_workable_absorption_coeff_water()[wavelength]
list_wavelengths = WIKI_workable_available_wavelengths()

T = 20
start_intensity = 0.100  # Watt/cm2

# lists for the plot
list_humidity = make_2d_humidity_list(101, 101)  # %
list_path_length = make_2d_path_length_list(101, 101)  # meter

list_intensity_loss = np.zeros((101, 101))

for i in range(len(list_humidity[0, :])):
    for j in range(len(list_path_length[0, :])):
        max_intensity_loss = WIKI_find_intensity_loss(start_intensity, list_path_length[j, 0],
                                                      absorption_coefficient_water, list_humidity[0, i], T)

        list_intensity_loss[i, j] = (max_intensity_loss / start_intensity) * 100

list_intensity_loss = 100 - list_intensity_loss

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(list_humidity, list_path_length, list_intensity_loss, rstride=10, cstride=10)
# ax.grid()
plt.title(f'Intensity loss at T = {T}C, [%]')
plt.ylabel('Path length (m)')
# ax.xlim((0,100))
plt.xlabel('Percentage Humidity')

plt.show()
