import numpy as np
from matplotlib import pyplot as plt
from scipy import fftpack

# Perform DCT on a frame and create the frame DCT array 
def frameDCT(Y):
    frameDCT = np.array([])
    for samples in range(Y.shape[1]):
        
        samplesDCT = fftpack.dct(Y[:,samples], type=4)
        frameDCT = np.append(frameDCT, samplesDCT)
        
    return frameDCT


# Perform inverse DCT on a frame's DCT array and retrieve the initial frame
def iframeDCT(c):
    
    frameFinal = np.zeros([36,32])
    for i in range(0,c.shape[0], 36):
        c1 = c[i:i+36]
        idct = fftpack.idct(c[i:i+36], type=4)
        frameFinal[:,int(i/36)] = idct/72
       
    return frameFinal
# np.random.seed(0)
# data = np.random.uniform(0,100, [36,32])

# dct = frameDCT(data)
# idct = iframeDCT(dct)

# fig = plt.figure()
# ax = plt.axes()
# print("DCT's max value: " , np.max(data))
# print("IDCT's Max Value : " , np.max(idct))
# print("")

# ax.plot(data - idct)
# plt.show()