import numpy as np
from matplotlib import pyplot as plt
import Dksparse
import DCTpower

# Find the DCT components that are likely to be tonal ones
def STinit(c: np.ndarray, D: np.ndarray) -> np.ndarray:
    
    
    P = DCTpower.DCTpower(c)
    ST = []
    
    # Iterate throught each DCT component and check if it meets the criteria
    # for being a masker. If it does, it is added to the initial tonal components list
    for k in range(0,c.shape[0]):
        
        Dk = [P*D[k,:]]
        Pk = P[k] - Dk - 7
        count = np.count_nonzero(Pk < 0)
        
        if k < P.shape[0]-1:
            if P[k] > P[k-1] and P[k] > P[k+1] and count == 0:
                ST.append(k)
        if k == P.shape[0]-1:
            if P[k] > P[k-1] and count == 0:
                ST.append(k)     
    return np.array(ST)


#data = np.random.uniform(0,100, [1152])

# data_1 = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,23,3,56,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
# data_power = DCTpower.DCTpower(data)
# dataFinal = np.concatenate((data,data_1))
# print(data.shape[0]


# D = Dksparse.Dksparse(data.shape[0])

# st1 = STinit(data, D)
# print(st1)
