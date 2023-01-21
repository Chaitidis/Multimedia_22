import numpy as np
from STinit import STinit
from STreduction import STreduction
from Masking_Thresholds import Masking_Thresholds
from Global_Masking_Thresholds import Global_Masking_thresholds

def psycho(c: np.ndarray, D: np.ndarray) -> np.ndarray:
    
    st = STinit(c, D)
    Tq = np.array(np.load('Tq.npy', allow_pickle=True).tolist()[0]) +30
    str, pmr = STreduction(st,c,Tq)
    Ti = Masking_Thresholds(str,pmr,c.shape[0])
    Tg = Global_Masking_thresholds(Ti, Tq)
    
    return Tg