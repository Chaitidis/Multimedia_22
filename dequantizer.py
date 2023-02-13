import numpy as np
from matplotlib import pyplot as plt
from quantizer import quantizer

def dequantizer(symb_index: np.ndarray, b: int) -> np.ndarray:
    
    zones = 2**b
    step = 1/(zones)
    
    #values = np.concatenate((np.linspace(-1+step/2 , 0-step, int((zones)/2)-1),np.linspace(0, 1- step/2, int((zones)/2))))
    values = np.arange(-1 +step, 1, 2*step)
    values[int(np.floor(zones/2))-1]  = 0
    values[int(np.ceil(zones/2)):]  = values[int(np.ceil(zones/2)):] +2*step
    xh = np.zeros(symb_index.shape[0])
    
    for i in range(len(xh)):
        xh[i] = values[symb_index[i]+int(zones/2)-1]    
    
    return xh

# np.random.seed(0)    
# data = np.linspace(-1,1,2000)

# quant= quantizer(data,4)

# deq = dequantizer(np.int16(quant), 4)

# fig = plt.figure()
# ax = plt.axes()

# ax.plot(data)
# ax.plot(deq)
# plt.show()
    