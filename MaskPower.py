import numpy as np
from matplotlib import pyplot as plt
from DCTpower import DCTpower
from Dksparse import Dksparse
from STinit import STinit

# Compute the power of each masker in the initial tonal components list
def MaskPower(c: np.ndarray, ST: np.ndarray) -> np.ndarray:
    
    P = DCTpower(c)
    PM = np.ndarray(ST.shape)
    
    k = 0
    
    # We compute the final value of the power of each masker, 
    # which takes the power of the adjacent DCT components into account  
    for i in ST:
        if i == 0:
            PM[k] = 10*np.log10(np.sum(10**(0.1*P[i:i+2])))
        elif i == c.shape[0] - 1:
            PM[k] = 10*np.log10(np.sum(10**(0.1*P[i-1:i+1])))  
        else:
            PM[k] = 10*np.log10(np.sum(10**(0.1*P[i-1:i+2])))         
        k+=1
    
    return PM


# data = np.random.uniform(0,100, [1152])

# D = Dksparse(data.shape[0])

# st1 = STinit(data, D)    

# mp1 = MaskPower(data, st1)
# print(data[st1[:]])
# print(mp1)