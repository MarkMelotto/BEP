from functions.functions import *

a0 = 6.107799961
a1 = 4.436518521e-1
a2 = 1.428945805e-2
a3 = 2.650648471e-4
a4 = 3.031240396e-6
a5 = 2.034080948e-8
a6 = 6.136820929e-11

T = 50
approximation = a0 + T*(a1+T*(a2 + T*(a3 + T*(a4 + T*(a5 + a6*T)))))
my_calc = calculate_water_saturation(T)

print(f"my water saturation = {my_calc}, approximation = {approximation}")