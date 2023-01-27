import numpy as np
from matplotlib import pyplot as plt
from quantizer import quantizer

def dequantizer(symb_index: np.ndarray, b: int) -> np.ndarray:
    
    zones = 2**b -1
    
    values = np.linspace((2/zones)-1,1- ((2/zones)), zones)
    
    xh = np.zeros(symb_index.shape[0])
    
    for i in range(len(xh)):
        xh[i] = values[symb_index[i]+128]    
    
    return xh

np.random.seed(0)    
data = np.random.uniform(-1,1, [100])

quant= quantizer(data,8)

deq = dequantizer(np.int16(quant), 8)

# fig = plt.figure()
# ax = plt.axes()

# ax.plot(data)
# ax.plot(deq)
# plt.show()
    