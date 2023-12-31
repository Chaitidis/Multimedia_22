import numpy as np
from matplotlib import pyplot as plt
from DCTpower import DCTpower
from MaskPower import MaskPower
from STinit import STinit
from Dksparse import Dksparse
from Hz2Barks import Hz2Barks

def STreduction(ST: np.ndarray,c: np.ndarray,Tq: np.ndarray) -> np.ndarray:
    
    PM = MaskPower(c, ST)
    
    # 1st Criterion: Remove maskers if their power is below hearing threshhold
    STr = []
    for i in range(len(ST)):
        if PM[i] > Tq[ST[i]]:
           STr.append(ST[i]) 
    
    STr = np.array(STr)
    PMr = MaskPower(c, STr)
    
    # Locate new maskers positions in Hz space
    # and convert them into Barks.
    hz = np.array([(i+1)*689/36 for i in range(len(STr))])
    barks = Hz2Barks(hz)
    
    to_remove = []
    
    # 2nd Criterion: Remove the smallest of all pairs of maskers
    # with distance <0.5 Barks from one another 
    for k in range(len(barks)-1):
        if k not in to_remove:    
            for j in range(k+1, len(barks)):
                if np.abs(barks[k] - barks[j]) <0.5 and k not in to_remove:
                    
                    to_remove.append(np.where(PMr == np.min([PMr[k], PMr[j]]))[0][0])
                  
    STr = np.delete(STr, to_remove)
    
    # Compute the power of the new maskers
    PMr = MaskPower(c, STr)
    
    return(STr,PMr)

