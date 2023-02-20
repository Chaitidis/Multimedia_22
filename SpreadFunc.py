import numpy as np
from Hz2Barks import Hz2Barks 
from MaskPower import MaskPower
from matplotlib import pyplot as plt

# We compute the spreading function in order to
# determine the areas that tonal components affect and how much they affect these areas.
def SpreadFunc(ST: np.ndarray,PM: np.ndarray, Kmax: int) -> np.ndarray:
    
    spread = np.ndarray([Kmax+1, ST.shape[0]])

    barks= Hz2Barks(np.array([(i+1)*689/36 for i in range(Kmax+1)]))
    
    # Compute the spreading function values
    # depending on the power of the masker,
    # as well as the distance (in Barks) from it
    for k in range(ST.shape[0]):
        for i in range(spread.shape[0]):
            Dz = barks[i] - barks[ST[k]]
            if  Dz >= -3 and  Dz < -1:
                spread[i,k] = 17*(Dz) - 0.4*PM[k] + 11
            elif Dz >= -1 and  Dz < 0:
                spread[i,k] = (0.4*PM[k] + 6)*Dz
            elif Dz >= 0 and  Dz < 1:
                spread[i,k] = -17*Dz
            elif Dz >= 1 and  Dz < 8:          
                spread[i,k] = (0.15*PM[k] - 17)*Dz - 0.15*PM[k]
            else: 
                spread[i,k] = -np.Infinity
    return spread


