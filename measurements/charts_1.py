from measurements.data import *
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D  # for legend handle

# skipping test 2 for now, as it has less data points and it sucks

tests = [test_1, test_3, test_4]  # all have 12 data points


# function to read the data out of my stored data
def test_data_reader(test):
    resistor = 0
    distance_lamp_to_box = 0
    distance_box_to_detector = 0
    humidity = []
    dark_voltage = []
    light_voltage = []
    temperature = []
    voltage_gain = []

    for k, v in test.items():
        if k == "system_data":
            resistor = v[0]
            distance_lamp_to_box = v[1]
            distance_box_to_detector = v[2]
        else:
            actual_voltage = v[1] - v[0]
            humidity.append(k)
            dark_voltage.append(v[0])
            light_voltage.append(v[1])
            temperature.append(v[2])
            voltage_gain.append(actual_voltage)

    return resistor, distance_lamp_to_box, distance_box_to_detector, humidity, dark_voltage, light_voltage, temperature, voltage_gain


# function to make nice colors for the plot
def color_magic(temp):
    temperature = temp
    min_temp = min(temperature)
    max_temp = max(temperature)
    difference = max_temp - min_temp

    some_dict = dict()
    test_ = []

    for T in temp:
        red_color = (T - min_temp) / difference
        # RGB = [red_color,red_color/1.5,0.545]
        RGB = [red_color, 0, red_color / 3]
        some_dict[T] = RGB
        test_.append(RGB)

    return some_dict, test_


data = []

for test in tests:
    resistor, distance_lamp_to_box, distance_box_to_detector, humidity, dark_voltage, light_voltage, temperature, \
    voltage_gain = test_data_reader(test)

    data.append({"resistor": resistor, "distance_lamp_to_box": distance_lamp_to_box,
                 "distance_box_to_detector": distance_box_to_detector, "humidity": humidity,
                 "dark_voltage": dark_voltage,
                 "light_voltage": light_voltage, "temperature": temperature, "voltage_gain": voltage_gain})

fig, axs = plt.subplots(len(data), figsize=(20, 15))

for i in range(len(data)):
    x = data[i]["humidity"]
    y = data[i]["voltage_gain"]
    temp = data[i]["temperature"]
    color_dict, color = color_magic(temp)
    axs[i].plot(x, y)
    axs[i].scatter(x, y, c=color)
    handles = [Line2D([0], [0], marker='o', color='w', markerfacecolor=v, label=k, markersize=8) for k, v in
               color_dict.items()]
    axs[i].legend(title='Temperature C', handles=handles, bbox_to_anchor=(1, 1), loc='upper left')

    axs[i].set_title(f'Voltage measure with the following parameters:\n'
                     f'Resistance = {data[i]["resistor"] / 1000} kOhm, distance lamp-box-sensor: '
                     f'{data[i]["distance_lamp_to_box"]}-{data[i]["distance_box_to_detector"]} cm')
    axs[i].grid()
    axs[i].set_xlabel(f'humidity (%)')
    axs[i].set_ylabel('mV')

plt.tight_layout()
plt.show()
plt.savefig("data")
