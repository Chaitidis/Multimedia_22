import numpy as np
from Hz2Barks import Hz2Barks
from SpreadFunc import SpreadFunc
from matplotlib import pyplot as plt


# Compute the values that indicate the impact
# of tonal components on the hearing threshold.
# These values will be used in the computation of the final hearing threshold
def Masking_Thresholds(ST: np.ndarray,PM: np.ndarray,Kmax: int) -> np.ndarray: 
    
    Ti = np.ndarray([Kmax+1, ST.shape[0]])
    barks = Hz2Barks(np.array([(i+1)*689/36 for i in range(Kmax+1)]))
    Sf = SpreadFunc(ST, PM , Kmax)
    
    # Compute the Ti values that correspond to each tonal component.
    for j in range(Ti.shape[1]):
        for i in range(Ti.shape[0]):
            Ti[i,j] = PM[j] - 0.275*barks[ST[j]] + Sf[i,j] - 6.025
    
    return Ti        


