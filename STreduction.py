import numpy as np
from matplotlib import pyplot as plt
from DCTpower import DCTpower
from MaskPower import MaskPower
from STinit import STinit
from Dksparse import Dksparse
from Hz2Barks import Hz2Barks

def STreduction(ST: np.ndarray,c: np.ndarray,Tq: np.ndarray) -> np.ndarray:
    
    PM = MaskPower(c, ST)
    STr = []
    for i in range(len(ST)):
        if PM[i] > Tq[ST[i]]:
           STr.append(ST[i]) 
    
    STr = np.array(STr)
    PMr = MaskPower(c, STr)
    
    hz = np.array([(i+1)*689/36 for i in range(len(STr))])
    barks = Hz2Barks(hz)
    
    to_remove = []
    
    for k in range(len(barks)-1):
        if k not in to_remove:    
            for j in range(k+1, len(barks)):
                if np.abs(barks[k] - barks[j]) <0.5 and k not in to_remove:
                    
                    to_remove.append(np.where(PMr == np.min([PMr[k], PMr[j]]))[0][0])
                  
    STr = np.delete(STr, to_remove)
    PMr = MaskPower(c, STr)
    return(STr,PMr)

#np.random.seed(1)

data = np.random.uniform(0,100,[1152])

Dk = Dksparse(1152)

Tq = np.load('Tq.npy', allow_pickle=True).tolist()[0]



st1 = STinit(data,Dk)

str1, pm1 = STreduction(st1, data,Tq)
#print(st1)
#print(str1)

# fig = plt.figure()
# ax = plt.axes()

# ax.plot(Tq)
# plt.show()