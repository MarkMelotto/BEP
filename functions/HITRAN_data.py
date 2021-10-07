'''some HITRAN data on the absorption coefficients on molecules all in 1/cm:'''
def HITRAN_get_mu_water():
    return {5344: 0.55, 7210: 0.4, 7400: 0.37, 8812: 0.03, 10700: 0.0129, 10638: 0.0006}

# def get_mu_nitrogen():
#     return {5344: -0.0275, 7210: -0.17, 7400: -0.14, 8812: -0.112, 10700: 0, 10638: 0}

def HITRAN_get_mu_nitrogen():
    return {5344: 0, 7210: 0, 7400: 0, 8812: 0, 10700: 0, 10638: 0}


def HITRAN_get_mu_oxygen():
    return {5344: 7.36E-6, 7210: 2.98E-5, 7400: 1.1E-5, 8812: 1.1E-5, 10700: 3.355E-5, 10638: 2.6E-5}


def HITRAN_get_mu_carbon_mono_oxide():
    return {5344: 0.0209, 7210: 3.36e-3, 7400: 3.11e-3, 8812: 2.490e-3, 10700: 3.86e-3, 10638: 4.11e-3}