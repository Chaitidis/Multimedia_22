import numpy as np
from Hz2Barks import Hz2Barks
from SpreadFunc import SpreadFunc
from matplotlib import pyplot as plt

def Masking_Thresholds(ST: np.ndarray,PM: np.ndarray,Kmax: int) -> np.ndarray: 
    
    Ti = np.ndarray([Kmax+1, ST.shape[0]])
    barks = Hz2Barks(np.array([(i+1)*689/36 for i in range(Kmax+1)]))
    Sf = SpreadFunc(ST, PM , Kmax)
    
    for j in range(Ti.shape[1]):
        for i in range(Ti.shape[0]):
            Ti[i,j] = PM[j] - 0.275*barks[ST[j]] + Sf[i,j] - 6.025
    
    return Ti        



data = np.random.uniform(0,100, [1152])


PM = np.random.uniform(0,100,[1152])
st1= np.arange(1152)

#PM=MaskPower(data, st1)
#PM = np.ones(st1.shape[0])*100
Ti1 = Masking_Thresholds(st1, PM, 1151)




# fig = plt.figure()
# ax = plt.axes(projection = '3d')



# for i in range(Ti1.shape[0]):
#     ax.scatter3D(np.ones(Ti1.shape[1])*i,np.arange(Ti1.shape[1]), Ti1[i,:] )
# plt.show()