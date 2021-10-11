import numpy as np


'''basic functions'''
# function to measure the intensity left over after a certain path length
def measure_intensity(start_intensity, atten_coef, length):
    return start_intensity * np.exp(-atten_coef * length)

# returns the difference in dB between start signal and end signal
def intensity_in_dB(start_intensity, current_intensity):
    return 10 * np.log10(current_intensity / start_intensity)

def wavenumber_to_wavelength(WN):
    return 0.01 / (WN)

# returns water saturation at g/m3
def calculate_water_saturation(T):
    return np.exp(1.56065404) * np.exp(6.90219321e-02 * T) * np.exp(-2.38543241e-04 * T ** 2)

# returns air density at kg/m3
def calculate_air_density(T):
    return 1.44685243e-05 * T ** 2 - 4.72481940e-03 * T + 1.29255728

# returns decimal percentage of the max percentage water in the air at certain temperature T
# accurate between -20 and 60 C
def calculate_maximum_percentage_water(T):
    water_saturation = calculate_water_saturation(T)  # g/m3
    air_density = calculate_air_density(T)  # kg/m3

    max_percentage = (water_saturation / (air_density * 1000))  # decimal percentage

    return max_percentage

def make_2d_humidity_list(x, y):
    humidity = np.zeros((x,y))
    for i in range(x):
        for j in range(y):
            humidity[i,j] = j

    return humidity

def make_2d_path_length_list(x, y):
    path_length = np.zeros((x,y))
    for i in range(x):
        for j in range(y):
            path_length[i,j] = i/(y-1)

    return path_length

if __name__ == "__main__":
    print(f"testing the decimal percentage water in air: {calculate_maximum_percentage_water(20)}")

    print(f"test for humidity 2d: \n{make_2d_humidity_list(101, 101)}")

    print(f"test for path_length 2d: \n{make_2d_path_length_list(101, 101)}")

