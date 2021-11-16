

R = 46.5e3
spectral_sensitivity = 0.9

while True:
    volt = input("gimme the voltage measured in mV\n")
    volt = float(volt)  # mVolt
    volt *= 1000  # Volt
    current = volt/R  # Ampere

    # current *= 1e6
    intensity = (current / 37) / spectral_sensitivity

    print(f"incoming intensity = {intensity} mW/cm2\n")