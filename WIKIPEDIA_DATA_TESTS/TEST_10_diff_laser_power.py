import numpy as np

available_laser_power = [30, 50, 100]           #mWatt
surface_area_detector = 6.5                     #mm2
diameter_laser = 10                            #mm
surface_area_laser = np.pi * (diameter_laser/2)**2  #mm2

for power in available_laser_power:
    power_at_laser_tip = power / surface_area_laser # mWatt/mm2
    power_at_laser_tip *= 100                      # mWatt/cm2
    print(f"a laser at {power} mWatt, shines at {power_at_laser_tip} mWatt/cm2")