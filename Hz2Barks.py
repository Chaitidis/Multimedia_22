import numpy as np

def Hz2Barks(f: np.ndarray) -> np.ndarray:
    
    barks = 13*np.arctan(0.00076*f) + 3.5*np.arctan((f/7500)**2)
    
    return barks