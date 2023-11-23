import numpy as np
from matplotlib import pyplot as plt


# Compute the sparse matri that indicates which DCT components belong to each possible masker's neighborhood Dk 
def Dksparse(Kmax: int) ->np.ndarray:
    
    sparse = np.zeros([Kmax,Kmax])
    
    
    # Where each neighborhood is placed is determined dynamically 
    # and does not depent on "Kmax" being equal to 1152.
    # Hence the "weird" decimals in the conditions
    for k in range(2,int(0.24479167*Kmax)):
        
        sparse[k,k-2] = 1
        sparse[k,k+2] = 1  

    for k in range(int(0.24479167*Kmax),int(0.49479167*Kmax)):
        for j in range(2,14):
            sparse[k,k-j] = 1
            sparse[k,k+j] = 1
    
    for k in range(int(0.49479167*Kmax),Kmax):
        for j in range(2,28):
            sparse[k,k-j] = 1
            if k+j < Kmax:
                sparse[k,k+j] = 1
    
    return sparse            


