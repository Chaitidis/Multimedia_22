import numpy as np
from Masking_Thresholds import Masking_Thresholds
from matplotlib import pyplot as plt
from MaskPower import MaskPower


# Determine the final hearing threshold,
# taking into account the effect of tonal components
def Global_Masking_thresholds(Ti: np.ndarray,Tq: np.ndarray) -> np.ndarray:
    
    Tg = np.ndarray([Ti.shape[0],])
    
    # Compute the threshold's each final value using
    # the values of Ti to add to the initial value   
    for i in range(Tg.shape[0]-1):
        Tg[i] = 10*np.log10(10**(0.1*Tq[i]) + np.sum(10**(0.1*Ti[i,:])))
        
    return Tg

 