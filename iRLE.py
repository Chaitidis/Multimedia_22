import numpy as np
from matplotlib import pyplot as plt
import RLE
from all_bands_quantizer import symb

def iRLE(run_symbols: np.ndarray, K: int) -> np.ndarray:
    
    symb_index = np.zeros(K)
    symb_index[0] = run_symbols[0,0]
    count = int(run_symbols[0,1])
    
    if count != 0: 
        symb_index[1:1+count] = 0
            
    counter = count + 1
    start = counter
    
    for i in range(1, len(run_symbols)):
        
        symb_index[counter] = run_symbols[i,0]
        count = int(run_symbols[i,1])
    
        if count != 0: 
            symb_index[counter+1:counter+1+count] = 0
            counter += count 
        counter += 1    
    
    return symb_index

symb1 = iRLE( RLE.rle, 1152)

# fig = plt.figure()
# ax = plt.axes()   

# ax.plot(symb1 - symb)
# plt.show()