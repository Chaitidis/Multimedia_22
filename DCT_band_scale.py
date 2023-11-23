import numpy as np
from matplotlib import pyplot as plt
from critical_bands import critical_bands

# Normalize each band by using the max value in it
def DCT_band_scale(c: np.ndarray) -> np.ndarray:
    
    scale = np.zeros(c.shape[0])
    bands = critical_bands(c.shape[0])
    factors = np.ndarray(np.unique(bands).shape[0])
    
    # Each DCT value is normalized according to the respective scale factor of each band
    for band in np.unique(bands): 
        
        factors[int(band)-1] = np.max((np.abs(c*[bands == band]))**(3/4))
        
        scale_i = np.sign(c)*(((np.abs(c*[bands == band]))**(3/4))/factors[int(band)-1])
        scale = scale + scale_i[0,:]
       
    return (scale, factors) 

   
