import numpy as np
from matplotlib import pyplot as plt
from critical_bands import critical_bands

def DCT_band_scale(c: np.ndarray) -> np.ndarray:
    
    scale = np.zeros(c.shape[0])
    bands = critical_bands(c.shape[0])
    factors = np.ndarray(np.unique(bands).shape[0])
    
    for band in np.unique(bands): 
        
        factors[int(band)-1] = np.max((np.abs(c*[bands == band]))**(3/4))
        
        scale_i = np.sign(c)*(((np.abs(c*[bands == band]))**(3/4))/factors[int(band)-1])
        scale = scale + scale_i[0,:]
       
    return (scale, factors) 

   
# np.random.seed(0)
# data = np.random.uniform(-100,100, [1152])

# scl, factor = DCT_band_scale(data)



# fig1 = plt.figure()
# ax1 = fig1.add_subplot(1,2,1)
# ax2 = fig1.add_subplot(1,2,2)

# ax1.plot(data)
# ax2.plot(scl)

# plt.show()