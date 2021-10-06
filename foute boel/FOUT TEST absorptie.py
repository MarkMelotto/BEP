import numpy as np
# at 1242.38nm wavelength we get the following parameters:

mu_h20 = 25
mu_argon = 522.49
mu_O2 = 6003.13
mu_N2 = 384.27

N2 = 0.78
O2 = 0.209
argon = 0.009
low_H2O = 0.001
high_H2O = 0.03

start_intensity = 0.1 #Watt
path_length = 0.1 #meter

mu_low_AIR = mu_argon*argon + mu_O2*O2 + N2*mu_N2 + mu_h20*low_H2O
mu_high_AIR = mu_argon*argon + mu_O2*O2 + N2*mu_N2 + mu_h20*high_H2O

I_low = start_intensity*np.exp(-mu_low_AIR*path_length)
I_high = start_intensity*np.exp(-mu_high_AIR*path_length)

print(f"In de hoop dat deze eerste test berekening goed gaat:\n"
      f"We hebben hier:\n"
      f"low humidity: {I_low:.3}\n"
      f"high humidity: {I_high:.3}\n"
      f"Hopelijk zit hier aardig verschil in :)")