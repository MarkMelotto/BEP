import numpy as np
import matplotlib.pyplot as plt

air_density = {-20:1.394, -15:1.367, -10:1.341, -5:1.316, 0:1.292, 5:1.268, 10:1.246, 15:1.225, 20:1.204,
               25:1.184, 30:1.164, 35:1.146, 40:1.127, 45:1.11, 50:1.093, 55:1.076, 60:1.06}

temp = []
density = []

for k, v in air_density.items():
    temp.append(k)
    density.append(v)

curve_fit = np.polyfit(temp, density, 2)
print(curve_fit)

temp_range = np.linspace(-20, 60, 160)
fitted_curve_data = []

for T in temp_range:
    fitted_curve = 1.44685243e-05 * T**2 -4.72481940e-03 * T +1.29255728
    fitted_curve_data.append(fitted_curve)

plt.plot(temp, density)
plt.plot(temp_range, fitted_curve_data, 'r-')
plt.show()