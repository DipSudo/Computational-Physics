import numpy as np 
import matplotlib.pyplot as plt

# Global constants 
g = 9.81  # gravitational constant 
v_o = 100 
# theta = np.deg2rad(30)

def main(angle): 
    
    theta = np.deg2rad(angle)
    x, y = [], []
    x_i, y_i = 0, 0 

    for t in np.arange(0, 1000, 0.01): 
            
            x_f = x_i + (v_o * np.cos(theta) * t)
            y_f = y_i + (v_o * np.sin(theta) * t) - (g * t**2)

            if y_f >= 0:  
                x.append(x_f)
                y.append(y_f)

            x_i, y_i = x_f, y_f

    plt.plot(x, y, label=f"{angle}\u00b0")  # Adding label for each trajectory


if __name__ == "__main__":

    for angles in range(30,91,15): 
        main(angles)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Projectile Motion with intial velocity of {v_o}m/s")
    plt.legend()
    plt.savefig("Projectile Motion plots at varying angles.png")
    plt.show()