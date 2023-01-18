import numpy as np
from dct import frameDCT, iframeDCT
from Dksparse import Dksparse
from psycho import psycho



def dosomething1(Yc: np.ndarray) -> np.ndarray:
    
    dct = frameDCT(Yc)
    Dk = Dksparse(Yc.shape[0]*Yc.shape[1]) 
    Tg = psycho(dct, Dk)
    
    return dct

def idosomething1(dct: np.ndarray) -> np.ndarray:
    
    Yc = iframeDCT(dct)
    
    
    return Yc