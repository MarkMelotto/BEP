

R = 46.5e3
# spectral_sensitivity = 0.9
spectral_sensitivity = input("what is the current spectral sensitivity?:\n")
spectral_sensitivity = float(spectral_sensitivity)

while True:
    volt = input("gimme the voltage measured in mV\n")
    volt = float(volt)  # mVolt
    volt *= 1e-3  # Volt
    current = volt/R  # Ampere
    current *= 1e6  # uA
    intensity = (current / 37) / spectral_sensitivity

    print(f"incoming intensity = {intensity} mW/cm2\n")