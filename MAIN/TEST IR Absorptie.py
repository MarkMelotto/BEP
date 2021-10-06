import numpy as np
# at 2857.14nm wavelength we get the following parameters:

# attenuation coefficient
mu_h20 = 80
mu_argon = 0.01 # do not know it at this time
mu_O2 = 0.1
mu_N2 = 0.02

# percentage of air composition
N2 = 0.78
O2 = 0.209
argon = 0.009
low_H2O = 0.001
high_H2O = 0.03

start_intensity = 0.100 #Watt/cm2
path_length = 0.1 #meter

mu_low_AIR = mu_argon*argon + mu_O2*O2 + N2*mu_N2 + mu_h20*low_H2O
mu_high_AIR = mu_argon*argon + mu_O2*(O2-0.01) + (N2-0.01)*mu_N2 + mu_h20*high_H2O

I_low = start_intensity*np.exp(-mu_low_AIR*path_length)
I_high = start_intensity*np.exp(-mu_high_AIR*path_length)

print(f"\n"
      f"We hebben hier:\n"
      f"low humidity: {I_low:.3} Watt/cm2, {10*np.log10(I_low/start_intensity)} dB\n"
      f"high humidity: {I_high:.3} Watt/cm2, {10*np.log10(I_high/start_intensity)} dB\n"
      f"Hopelijk zit hier aardig verschil in :)\n"
      f"er is een verschil van {I_low/I_high-1:.3}%\n"
      f"a change of {10*np.log10(I_low/start_intensity)- 10*np.log10(I_high/start_intensity)} dB")