'''DATA wikipedia in 1/m'''

def WIKI_get_absorption_coeff_water():
    return {718e-9:1, 810e-9:1.5, 940e-9:20, 980e-9:10, 1.15e-6:100, 1.38e-6:30, 1.88e-6:900, 2.68e-6:8000, 6.3e-6:15000}

def WIKI_available_wavelengths():
    return [718e-9, 810e-9, 940e-9, 980e-9, 1.15e-6, 1.38e-6, 1.88e-6, 2.68e-6, 6.3e-6]

def WIKI_get_workable_absorption_coeff_water():
    return {718e-9:1, 810e-9:1.5, 940e-9:20, 980e-9:10, 1.15e-6:100, 1.38e-6:30}

def WIKI_workable_available_wavelengths():
    return [718e-9, 810e-9, 940e-9, 980e-9, 1.15e-6, 1.38e-6]