import control as ct
import numpy as np
from . import utils as dof

def two_degrees_system(system):
    A = dof.get_A_2dof(system)
    B = dof.get_B_2dof(system)
    C = dof.get_C_2dof(system)
    return [A, B, C]
