import numpy as np


def get_A_2dof(system):
    numerator = system.num[0][0].tolist()
    denominator = system.den[0][0].tolist()
    denominator.reverse()
    denominator.pop()
    order = len(denominator)
    A = np.zeros((2 * order, 2 * order))
    for i in range(2 * len(denominator)):
        for j in range(2 * len(denominator)):
            if (j == i + 1 and i != 2 * len(denominator)):
                A[i, j] = 1
            elif (i + 1 == len(denominator) and j + 1 <= order):
                A[i, j] = denominator[i]
            elif(i + 1 == len(denominator) and j + 1 > order):
                if( i + 1 <= len(numerator)):
                    A[i, j] = numerator[i - order + 1]
                else:
                    A[i, j] = 0
    return A

def get_B_2dof(system):
    denominator = system.den[0][0].tolist()
    denominator.pop()
    order = len(denominator)
    B = np.zeros((2 * order, 1))
    B[2 * order - 1, 0] = 1
    return B

def get_C_2dof(system):
    denominator = system.den[0][0].tolist()
    denominator.pop()
    order = len(denominator)
    C = np.zeros((1, 2 * order))
    C[0,0] = 1
    return C
