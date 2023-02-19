import numpy as np
from STinit import STinit
from STreduction import STreduction
from Masking_Thresholds import Masking_Thresholds
from Global_Masking_Thresholds import Global_Masking_thresholds

# Combine all steps regarding the psychoacoustic phenomenon
# to compute the final hearing threshold of a frame of DCT components
# that is produced due to possible tones that may exist in it
def psycho(c: np.ndarray, D: np.ndarray) -> np.ndarray:
    
    st = STinit(c, D)
    
    # We moved the values of the thresholds up and down to find the most realistic
    # interpretation of the impact of tonal components on the hearing threshold   
    Tq = np.array(np.load('Tq.npy', allow_pickle=True).tolist()[0]) +30
    
    str, pmr = STreduction(st,c,Tq)
    Ti = Masking_Thresholds(str,pmr,c.shape[0])
    Tg = Global_Masking_thresholds(Ti, Tq)
    
    # This adjustment just makes the "spikes" in the thresholds smaller in amplitude
    return Tg - 30