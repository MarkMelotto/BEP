import numpy as np

L = 0.1 #meter
focal_point_1 = 0.02 #meter
focal_point_2 = 0.02 #meter

def propagating_homogeneous_matrix(distance):
    return np.array([[1,0],[distance,1]])

def lens_focal_matrix(focal):
    return np.array([[1, -1/focal], [0, 1]])

def starting_point(angle,position):
    return np.array([angle, position])

if __name__ == "__main__":

    transfer_matrix = lens_focal_matrix(focal_point_2) @ propagating_homogeneous_matrix(L) @ lens_focal_matrix(focal_point_1)

    print(transfer_matrix)