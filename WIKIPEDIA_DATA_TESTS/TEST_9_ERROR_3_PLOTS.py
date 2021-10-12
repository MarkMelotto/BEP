from functions.WIKI_functions import *
from functions.WIKI_data import *
from functions.functions import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

absorption_coefficient_water = WIKI_get_workable_absorption_coeff_water()
list_wavelengths = WIKI_workable_available_wavelengths()
wavelength = 940e-9

random_temperature = True
start_intensity = 0.100  # Watt/cm2
path_length_list = make_2d_path_length_list(101, 101)  # meter
path_length_list = path_length_list[:,:3]
path_length_list = path_length_list[1:,:] # dont want the the path length of 0

# decimals rounded
decimal_round_list = make_2d_decimal_list(100)

# number of iterations
N = 10000
if not random_temperature:
    T = 10

error_list = np.zeros((101,3))

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

            # to make this work as a real life situation, we cannot measure at 10 decimals
            # print(decimal_round_list[0,j])
            random_intensity = round(random_intensity, int(decimal_round_list[0,j]))

            humidity = WIKI_find_humidity_from_intensity_at_T(start_intensity, random_intensity, path_length_list[i,0],
                                                         absorption_coefficient_water[wavelength], T)

            temp_error_list.append(abs(humidity-REAL_humidity))
        error_list[i,j] = sum(temp_error_list)/len(temp_error_list)
            # print(f"\n"
            #       f"for wavelength: {wavelength * 1e9:.2f} nm over a path length of {path_length * 100} cm at T = {T}:\n"
            #       f"The real humidity is: {REAL_humidity} %\n"
            #       f"Calculated humidity is: {humidity} %\n")

error_list = error_list[1:,:] # first row are nan
# decimal_round_list = decimal_round_list[1:,:]
# path_length_list = path_length_list[1:,:]
print(error_list)

# errors = error_list.flatten()


print(np.array(error_list[:,0]).shape)
fig, axs = plt.subplots(3, 1, sharex='col')
axs[0].plot(path_length_list[:-1,0], error_list[:-1,0])
axs[0].set_title("Mean error % in the 1 mWatt range")

axs[1].plot(path_length_list[:-1,0], error_list[:-1,1])
axs[1].set_title("Mean error % in the .1 mWatt range")

axs[2].plot(path_length_list[:-1,0], error_list[:-1,2])
axs[2].set_title("Mean error % in the .01 mWatt range")

for i in range(3):
    axs[i].grid()
    axs[i].set_xlabel('light path length (m)')
    axs[i].set_ylabel('%')

plt.tight_layout()
plt.show()