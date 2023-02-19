import numpy as np

# Convert an array of Hz values to their respective Barks values
def Hz2Barks(f: np.ndarray) -> np.ndarray:
    
    # convert the Hz values to Barks values 
    barks = 13*np.arctan(0.00076*f) + 3.5*np.arctan((f/7500)**2)
    
    return barks