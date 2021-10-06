import numpy as np

'''The Buck equation test for Vapour pressure of water'''

T = 10 #Celsius


pressure = 0.61121*np.exp((18.678-(T/123.5))*(T/(257.14+T)))

# print(f'at T={T} celsius, P = {pressure:.3} kPa')

labda = 810e-9

def calc_intensity(labda):
    h = 6.626e-34
    c = 3e8
    v = c / labda
    e = 1.6e-19
    E = h * v / e
    print(f'{E} eV')
    return E

def calc_wavelength(MeV):
    v = (MeV/1e6 * 1.6e-19 )/6.626e-34
    return 3e8 / v

print(calc_wavelength(0.005))
