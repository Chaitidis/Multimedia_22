import numpy as np
from matplotlib import pyplot as plt

def quantizer(x: np.ndarray,b: int) -> np.ndarray:
    
    zones = 2**b -1
    lim = np.zeros(zones+1)
    symb_index = np.zeros(len(x))
    for i in range(zones+1):
        lim[i] = (2*i/(zones+1)) - 1
        
    for i in range(len(x)):
        if np.sign((lim-x[i])[np.abs(lim-x[i]).argmin()]) < 0:
            floor = np.abs(lim-x[i]).argmin()
            symb_index[i] =  floor - len(lim)/2
        else:
            ceil = np.abs(lim-x[i]).argmin()
            symb_index[i] =  ceil - (len(lim)/2 +1)
        test=(lim-x[i])
        print(test)        
            
    return symb_index        




np.random.seed(0)
data = np.random.uniform(-1,1, [100])

quant= quantizer(data,8)



fig1 = plt.figure()
ax1=plt.axes()
ax1.plot(quant)
ax1.plot(data)
plt.show()