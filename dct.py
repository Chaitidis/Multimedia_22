import numpy as np
from scipy import fft
from matplotlib import pyplot as plt

def frameDCT(Y):
    flatFrame = Y.T.flatten()
    dct = fft.dct(flatFrame)
    return dct

def iframeDCT(Y):
    idct = fft.idct(Y)
    frame = idct.reshape((36,32))
    return frame



data = np.random.random([36,32])



dct = frameDCT(data)

frame = iframeDCT(dct)
print(dct)
fig = plt.figure()
ax = plt.axes()

ax.plot(data-frame)
plt.show()