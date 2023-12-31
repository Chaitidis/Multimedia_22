import numpy as np
from matplotlib import pyplot as plt
import RLE
from all_bands_quantizer import symb

# Perform inverse RLE and retrieve the initial symbol array 
def iRLE(run_symbols: np.ndarray, K: int) -> np.ndarray:
    
    symb_index = np.zeros(K)
    symb_index[0] = run_symbols[0,0]
    count = int(run_symbols[0,1])
    
    if count != 0: 
        symb_index[1:1+count] = 0
            
    counter = count + 1
    start = counter
    
    # Translate the symbols using their RLE representation
    for i in range(1, len(run_symbols)):
        
        symb_index[counter] = run_symbols[i,0]
        count = int(run_symbols[i,1])
    
        if count != 0 and counter < 1152: 
            symb_index[counter+1:counter+count] = 0
            counter += count 
        counter += 1    
    
    return symb_index
