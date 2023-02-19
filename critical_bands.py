import numpy as np
from matplotlib import pyplot as plt


# Compute the critical band that each DCT component belongs in
def critical_bands(K: np.ndarray) -> np.ndarray:
    
    Hz = np.array([(i+1)*689/36 for i in range(K)])
    cb = np.ndarray([Hz.shape[0]])
    
    # critical bands limits
    bands = [100, 200, 300, 400, 510, 630, 770, 920, 1080, 1270, 1480, 1720, 2000, 2320, 2700, 3150, 3700, 4400, 5300, 6400, 7700, 9500, 12000, 15500]
    
    # Determine the bands for the respective DCT component postitions
    cb[0: np.argwhere(Hz <=bands[0]).reshape(-1,)[-1]+1] = 1
    for i in range(0, len(bands)-1):
        cb[np.argwhere(Hz >= bands[i]).reshape(-1,)[0]:np.argwhere(Hz <=bands[i+1]).reshape(-1,)[-1]+1] = i + 2 
    cb[np.argwhere(Hz > bands[-1])[0,0]: len(cb)] = len(bands)+1
    
    return cb
    
    
# bands = critical_bands(1152)
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(bands)    
    
# plt.show()    
    
    
    