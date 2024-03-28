import numpy as np 

# Global constants 
g = 9.81  # gravitational constant 
v_o = 200  #speed of cannon 

#part 1 


def angle(x_f,x_i) -> float:    #angle of cannon from horizontal component 
    theta = 0.5*(np.arcsin((g*(x_f-x_i)/v_o**2)))
    theta = np.rad2deg(theta)
    return theta

print(angle(100,0))