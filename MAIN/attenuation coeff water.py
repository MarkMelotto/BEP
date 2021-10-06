import numpy as np

# wavelength:attenuation coefficient gepakt van wikipedia
attenuation_coefficients = {
    718e-9:1,
    810e-9:1.5,
    1.13e-6:20,
    1.38e-6:30,
    1.88e-6:900,
    2.68e-6:8000,
    6.3e-6:15000
}
# function to measure the intensity left over after a certain length
def measure_intensity(intensity, atten_coef, length):
    return intensity*np.exp(-atten_coef*length)

intensity_laser = 100e-3 #Watt
x = 0.1 #meter

# so for pure water this happens:
for k,d in attenuation_coefficients.items():
    new_intensity = measure_intensity(intensity_laser,d, x)
    print(f"for wavelength: {k*1e9} nanometer over a lenght: {x} meter, we end up with an intensity of: {new_intensity:.3} Watt/m2 \n"
          f"that is {(new_intensity/intensity_laser *100):.3f}% of the original\n ")