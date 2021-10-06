import numpy as np



'''
nitrogen:   78%     https://physics.nist.gov/PhysRefData/XrayMassCoef/ElemTab/z07.html
oxygen:     20.9%   https://physics.nist.gov/PhysRefData/XrayMassCoef/ElemTab/z08.html
argon:      0.93%   https://physics.nist.gov/PhysRefData/XrayMassCoef/ElemTab/z18.html
water:      0.1-3%  
'''
def calc_wavelength(MeV):
    v = (MeV/1e6 * 1.6e-19 )/6.626e-34
    return 3e8 / v

# all taken at 20C at https://www.engineeringtoolbox.com/oxygen-O2-density-specific-weight-temperature-pressure-d_2082.html
rho_nitrogen = 1.1606 #kg/m3
rho_oxygen = 1.314
rho_argon = 1.641

# data nitrogen MeV: mu/rho
nitrogen_data = {
    1e-3:3.311e3, 1.5e-3:1.082e3, 2e-3:4.769e2, 3e-3:1.456e2, 4e-3:6.166e1, 5e-3:3.144e1, 6e-3:1.809e1
}

argon_data = {
    1e-3:3.184e3, 1.5e-3:1.105e3, 2e-3:5.12e2, 3e-3:1.703e2, 4e-3:7.572e2, 5e-3:4.225e2, 6e-3:2.593e2
}

oxygen_data = {
    1e-3:4.59e3, 1.5e-3:1.549e3, 2e-3:6.949e2, 3e-3:2.171e2, 4e-3:9.315e1, 5e-3:4.79e1, 6e-3:2.77e1
}

def real_deal(dictio, rho):

    for k,v in dictio.items():
        labda = calc_wavelength(k)
        mu = rho*0.1*v
        print(f"wavelength: {labda:.2f} nm, attenuation coeff: {mu:.2f} ")

if __name__ == "__main__":
    print("Nitrogen:")
    real_deal(nitrogen_data, rho_nitrogen)
    print("")
    print("Oxygen:")
    real_deal(oxygen_data, rho_oxygen)
    print("")
    print("Argon:")
    real_deal(argon_data, rho_argon)
    print("")
