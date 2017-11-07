from optimal2dofcontrollers import representation as r
import control as ctr
import numpy as np

system = ctr.tf([0.0169],[1,0.1312,0.0043])
[A,B,C] = r.two_degrees_system(system)
