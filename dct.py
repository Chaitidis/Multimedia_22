import numpy as np
from scipy import fftpack
from matplotlib import pyplot as plt

def frameDCT(Y):
    frameDCT = np.array([])
    for samples in range(Y.shape[1]):
        samplesDCT = fftpack.dct(Y[:,samples], type=4)
        frameDCT = np.append(frameDCT, samplesDCT)
        print(1)
    return frameDCT

def iframeDCT(c):
    print(c)
    
    
    frameFinal = np.ndarray([36,32])
    print(frameFinal.shape)
    for i in range(0,c.shape[0], 36):
        idct = fftpack.idct(c[i:i+36], type=4)
        frameFinal[:,int(i/36)] = idct
        print(frameFinal)

        
    return frameFinal



data = np.random.random([36,32])



dct = frameDCT(data)

frame = iframeDCT(dct)
print(data-frame)
fig = plt.figure()
ax = plt.axes()

ax.plot(data-frame)
plt.show()