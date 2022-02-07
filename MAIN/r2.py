from functions.functions import *

real_air_density = {-20:1.394, -15:1.367, -10:1.341, -5:1.316, 0:1.292, 5:1.268, 10:1.246, 15:1.225, 20:1.204,
               25:1.184, 30:1.164, 35:1.146, 40:1.127, 45:1.11, 50:1.093, 55:1.076, 60:1.06}

real_water_sat = {-20:1.07, -10:2.28, -5:3.38, 0:4.83, 2:5.57, 4:6.36, 8:8.24, 10:9.36,
            12:10.6, 14:11.99, 16:13.53, 18:15.25, 20:17.15, 22:19.25, 24:21.58,
            25:22.83, 30:30.08, 35:39.23, 40:50.67, 50:82.23, 60:130} #T:g/m3

R_air_density = []
R_water_saturation = []

R_sum_air_density = []
R_sum_water_saturation = []

air_dens_for_mean = []
wat_sat_for_mean = []

for k, v in real_air_density.items():
    residual_air = v - calculate_air_density(k)
    R_air_density.append(residual_air**2)
    air_dens_for_mean.append(v)

for k, v in real_water_sat.items():
    residual_hum = v - calculate_water_saturation(k)
    R_water_saturation.append(residual_hum**2)
    wat_sat_for_mean.append(v)


SSR_air_dens = sum(R_air_density)
SSR_water_sat = sum(R_water_saturation)

mean_air_density = sum(air_dens_for_mean)/len(air_dens_for_mean)
mean_water_saturation = sum(wat_sat_for_mean)/len(wat_sat_for_mean)

for k, v in real_air_density.items():
    residual_air = v - mean_air_density
    R_sum_air_density.append(residual_air**2)

for k, v in real_water_sat.items():
    residual_hum = v - mean_water_saturation
    R_sum_water_saturation.append(residual_hum**2)

SST_air_dens = sum(R_sum_air_density)
SST_water_sat = sum(R_sum_water_saturation)

print(f"R2 air density = {1-(SSR_air_dens/SST_air_dens):4f}")
print(f"R2 water saturation = {1-(SSR_water_sat/SST_water_sat):4f}")