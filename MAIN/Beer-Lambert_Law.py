import numpy as np

''' A = elc'''

def absorbance(e,l,c):
    absorptivity = e
    length = l
    concentration = c
    absorb = absorptivity*length*concentration
    print(f'The absorbance = {absorb}')


'''A = sum, i=1 tot N, e int(0-l)c(z) dz'''
# attenuation_cross_section =
# number_density =
# absorptivity =
# amount_concentration =
# length =

if __name__ == "__main__":
    absorbance(0.6,0.1,8.3)