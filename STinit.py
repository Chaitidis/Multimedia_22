import numpy as np
from matplotlib import pyplot as plt
import Dksparse
import DCTpower

# Find the DCT components that are likely to be tonal ones
def STinit(c: np.ndarray, D: np.ndarray) -> np.ndarray:
    
    
    P = DCTpower.DCTpower(c)
    ST = []
    
    # Iterate throught each DCT component and check if it meets the criteria
    # for being a masker. If it does, it is added to the initial tonal components list
    for k in range(0,c.shape[0]):
        
        Dk = [P*D[k,:]]
        Pk = P[k] - Dk - 7
        count = np.count_nonzero(Pk < 0)
        
        if k < P.shape[0]-1:
            if P[k] > P[k-1] and P[k] > P[k+1] and count == 0:
                ST.append(k)
        if k == P.shape[0]-1:
            if P[k] > P[k-1] and count == 0:
                ST.append(k)     
    return np.array(ST)


