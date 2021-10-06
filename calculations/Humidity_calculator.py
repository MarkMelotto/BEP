import numpy as np
import matplotlib.pyplot as plt

# returns the saturated vapor pressure in mbar
def calculate_saturated_vapor_pressure(T_air):
    return 6.11*10**((7.5*T_air)/(237.3+T_air))

def calculate_actual_vapor_pressure(T_dewpoint):
    return 6.11*10**((7.5*T_dewpoint)/(237.3+T_dewpoint))

def relative_humidity(T_air, T_dewpoint):
    return calculate_actual_vapor_pressure(T_dewpoint)/calculate_saturated_vapor_pressure(T_air) * 100

humidity = {-20:1.07, -10:2.28, -5:3.38, 0:4.83, 2:5.57, 4:6.36, 8:8.24, 10:9.36,
            12:10.6, 14:11.99, 16:13.53, 18:15.25, 20:17.15, 22:19.25, 24:21.58,
            25:22.83, 30:30.08, 35:39.23, 40:50.67, 50:82.23, 60:130} #T:g/m3

x = []
y = []

for k, v in humidity.items():
    x.append(k)
    y.append(v)


log_x_data = np.log(x)
log_y_data = np.log(y)

curve_fit = np.polyfit(x, log_y_data, 2)
print(curve_fit)

# x_fit, y_fit = curve_fit[0], curve_fit[1]
# x_fit, y_fit = float(x_fit), float(y_fit)
# y_line = []
# for i in x:
#     y_line.append(np.exp(y_fit) * np.exp(x_fit * x))

x_fit = np.linspace(-20, 60, 160)
y_fit = []

# first order
# for z in x_fit:
#     y_line = np.exp(1.56) * np.exp(0.0594 * z)
#     y_fit.append(y_line)

# for second order
for z in x_fit:
    y_line = np.exp(1.56065404) * np.exp(6.90219321e-02 * z) * np.exp(-2.38543241e-04 * z**2)
    y_fit.append(y_line)


plt.plot(x,y)
plt.plot(x_fit, y_fit, 'r-')
plt.yscale("log")
plt.show()