import numpy as np


def DCTpower(c:np.ndarray) -> np.ndarray:
    
    power = 10*np.log10(c**2)
    
    return power

