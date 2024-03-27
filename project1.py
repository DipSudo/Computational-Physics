import numpy as np
import matplotlib.pyplot as plt


#global constants 

g = 9.81 #gravitational constant 
x_i = 0 
y_i = 0 
v_o = 100
theta = np.deg2rad(30)


def motion_x (t:float) -> float: 
    
    x_f = x_i + ((v_o * np.cos(theta)) *t)
    
    return x_f

def motion_y (t:float) -> float: 
    
    y_f = y_i + ((v_o * np.sin(theta)) *t) - (g*t**2)/2
    
    return y_f



def main(): 

    x, y = [],[]

    for i in range(0,101): 
        x.append(motion_x(i))
        y.append(motion_y(i))

    for x_coord, y_coord in zip(x, y):
        print(f"x: {x_coord}, y: {y_coord}")
    
    plt.plot(x,y)
    plt.show()

if __name__ == "__main__":
    main()