import numpy as np
from Masking_Thresholds import Masking_Thresholds
from matplotlib import pyplot as plt
from MaskPower import MaskPower

def Global_Masking_thresholds(Ti: np.ndarray,Tq: np.ndarray) -> np.ndarray:
    
    Tg = np.ndarray([Ti.shape[0],])
    
    for i in range(Tg.shape[0]-1):
        Tg[i] = 10*np.log10(10**(0.1*Tq[i]) + np.sum(10**(0.1*Ti[i,:])))
        
    return Tg

# Tq = np.array(np.load('Tq.npy', allow_pickle=True).tolist()[0])

# data = np.random.uniform(0,100, [1152])

# #st1= np.arange(0,1152, 1000)
# st1 = np.array([ 107,430, 720])
# #PM = np.random.uniform(0,100,[1152])

# #PM=MaskPower(data, st1)
# PM = np.array([ 10, 15,  50])

# #PM = np.ones(st1.shape[0])*100
# Ti1 = Masking_Thresholds(st1, PM, 1151)
# Tg = Global_Masking_thresholds(Ti1, Tq)





# fig = plt.figure()
# ax = plt.axes()

# #ax.plot(Ti1[:,1])
# ax.plot(Tg)
# ax.plot(Tq) 

# plt.show()   
    