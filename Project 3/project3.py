import numpy as np 
import random 
import math 

def Random_Walk(N,K) -> float:  #function that calculates the random direction travel 
    
    directions:str = ["North", "South", "East", "West"]
    total_distance:int = 0 
    
    x,y = 0,0  #initial position 
    
    for _ in range(K): 
        for _ in range(N):
             direction = random.choice(directions)
             
             if direction == "North":
                 y += 1
             elif direction == "South": 
                 y -= 1 
             elif direction == "West":
                 x -= 1 
             elif direction == "East":
                 x += 1 
        
        distance = math.sqrt(x**2 + y**2)
        total_distance += distance        

        
    
    return distance
    
if __name__ == "__main__":
    K = 1000  # Number of random walks
    N = 1000  # Maximum number of steps in a single walk
    R= Random_Walk(K, N) / K
    
    a = np.log(R)/np.log(N)
    print(f"Average distance from the origin after {N} steps in {K} random walks: {R}")
    print(f"Exponent A is ~{a}")