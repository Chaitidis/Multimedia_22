import numpy as np
from matplotlib import pyplot as plt
from dequantizer import dequantizer
from all_bands_quantizer import all_bands_quantizer
import all_bands_quantizer
from critical_bands import critical_bands


# Dequantize the symbols generated by all_bands_quantizer
def all_bands_dequantizer(symb_index: np.ndarray, B: np.ndarray, SF: np.ndarray) -> np.ndarray:
    
    xh = np.zeros(symb_index.shape[0])
    bands = critical_bands(symb_index.shape[0])
    
    # Append the right values to the symbols of each band using the appropriate number of bits 
    for band in np.unique(bands):
        start = np.where(bands==band)[0][0]
        end = np.where(bands==band)[0][-1] + 1
        dequant = dequantizer(symb_index[start:end], B[int(band-1)])
        xh[start:end] = np.sign(dequant)*np.abs(dequant*SF[int(band-1)])**(4/3)
        
    return xh

