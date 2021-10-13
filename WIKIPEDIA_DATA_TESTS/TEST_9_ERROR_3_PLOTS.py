from functions.WIKI_functions import *
from functions.WIKI_data import *
from functions.functions import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# getting the required data
absorption_coefficient_water = WIKI_get_workable_absorption_coeff_water()
list_wavelengths = WIKI_workable_available_wavelengths()

# choosing our wavelength
wavelength = 940e-9

start_intensity = 0.100  # Watt/cm2
path_length_list = make_2d_path_length_list(101, 101)  # meter
path_length_list = path_length_list[:,:3]
path_length_list = path_length_list[1:,:] # dont want the the path length of 0

# decimals rounded
decimal_round_list = make_2d_decimal_list(100)

# number of iterations
N = 10000

# if we want to control the temperature, we do that here
random_temperature = True
if not random_temperature:
    T = 10

error_list = np.zeros((100,3))

for i in range(len(path_length_list[:,0])):
    for j in range(len(decimal_round_list[0,:])):
        temp_error_list = []
        for _ in range(N):
            REAL_humidity = np.random.randint(0, 100)  # %
            if random_temperature:
                T = np.random.randint(-20, 60)

            concentration_water = WIKI_absorption_coefficient_air_composition_high_humidity_at_T(absorption_coefficient_water[wavelength], T)

            max_intensity_loss = measure_intensity(start_intensity, concentration_water, path_length_list[i, 0])

            random_intensity = ((max_intensity_loss - start_intensity) * REAL_humidity / 100) + start_intensity

            #measuring at different decimals (3,4,5)
            random_intensity = round(random_intensity, int(decimal_round_list[0,j]))

            humidity = WIKI_find_humidity_from_intensity_at_T(start_intensity, random_intensity, path_length_list[i,0],
                                                         absorption_coefficient_water[wavelength], T)

            temp_error_list.append(abs(humidity-REAL_humidity))
        error_list[i,j] = sum(temp_error_list)/len(temp_error_list)

error_list = error_list[1:,:] # first row are nan

# making the plots
fig, axs = plt.subplots(3, 1, sharex='col')
axs[0].plot(path_length_list[:-1,0], error_list[:,0])
axs[0].set_title(f"Mean error in the 1 mWatt range, LLN at N = {N}")

axs[1].plot(path_length_list[:-1,0], error_list[:,1])
axs[1].set_title(f"Mean error in the .1 mWatt range, LLN at N = {N}")

axs[2].plot(path_length_list[:-1,0], error_list[:,2])
axs[2].set_title(f"Mean error in the .01 mWatt range, LLN at N = {N}")

for i in range(3):
    axs[i].grid()
    axs[i].set_xlabel('light path length (m)')
    axs[i].set_ylabel('%')

plt.tight_layout()
plt.show()