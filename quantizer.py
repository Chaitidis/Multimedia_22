import numpy as np
from matplotlib import pyplot as plt


# Quantize an array of values into symbols that can be represented with b bits. 
def quantizer(x: np.ndarray,b: int) -> np.ndarray:
    
    # Compute the decision areas and zones 
    zones = 2**b
    lim = np.linspace(-1, 1, zones+1)
    # The list of symbols contains the value '0' twice
    # to indicate the merge of the two median bands around zero
    symb_list = np.concatenate((np.arange(-zones/2 +1, 1, 1), np.arange(0,zones/2, 1)))
    
    symb_index = np.zeros(len(x))
    
    # Find the closest zone value to the respective array value and append the right symbol     
    for i in range(len(x)):
        if np.sign((lim-x[i])[np.abs(lim-x[i]).argmin()]) < 0:
            floor = np.abs(lim-x[i]).argmin()
            symb_index[i] =  symb_list[floor]
        elif np.sign((lim-x[i])[np.abs(lim-x[i]).argmin()]) == 0 and np.abs(lim-x[i]).argmin() == 0:
            floor = np.abs(lim-x[i]).argmin()
            symb_index[i] =  symb_list[floor]
                   
        else:
            ceil = np.abs(lim-x[i]).argmin()
            symb_index[i] =  symb_list[ceil-1]
        test=(lim-x[i])
                
            
    return symb_index        




# np.random.seed(0)
# data = np.random.uniform(-1,1, [100])

# quant= quantizer(data,8)



# fig1 = plt.figure()
# ax1=plt.axes()
# ax1.plot(quant)
# ax1.plot(data)
# plt.show()