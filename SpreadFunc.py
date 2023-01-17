import numpy as np
from Hz2Barks import Hz2Barks 
from MaskPower import MaskPower
from matplotlib import pyplot as plt

def SpreadFunc(ST: np.ndarray,PM: np.ndarray, Kmax: int) -> np.ndarray:
    
    spread = np.ndarray([Kmax+1, ST.shape[0]])

    barks= Hz2Barks(np.array([(i+1)*689/36 for i in range(Kmax+1)]))
    
    
    for k in range(ST.shape[0]):
        for i in range(spread.shape[0]):
            Dz = barks[i] - barks[ST[k]]
            if  Dz >= -3 and  Dz < -1:
                spread[i,k] = 17*(Dz) - 0.4*PM[k] + 11
            elif Dz >= -1 and  Dz < 0:
                spread[i,k] = (0.4*PM[k] + 6)*Dz
            elif Dz >= 0 and  Dz < 1:
                spread[i,k] = -17*Dz
            elif Dz >= 1 and  Dz < 8:          
                spread[i,k] = (0.15*PM[k] - 17)*Dz - 0.15*PM[k]
            else: 
                spread[i,k] = -np.Infinity
    return spread



# data = np.random.uniform(0,100,[1152])
# st1= np.arange(1152)
# print(data)
# #PM=MaskPower(data, st1)
# PM = np.ones(st1.shape[0])*100
# spread1=SpreadFunc(st1, PM, 1151)
# print(spread1)

# fig = plt.figure()
# ax = plt.axes(projection = '3d')



# for i in range(spread1.shape[0]):
#     ax.scatter3D(np.ones(spread1.shape[1])*i,np.arange(spread1.shape[1]), spread1[i,:] )
# plt.show()