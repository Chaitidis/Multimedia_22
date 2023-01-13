import numpy as np
from scipy import fftpack


def frameDCT(Y):
    frameDCT = np.array([])
    for samples in range(Y.shape[1]):
        
        samplesDCT = fftpack.dct(Y[:,samples], type=4)
        frameDCT = np.append(frameDCT, samplesDCT)
        
    return frameDCT

def iframeDCT(c):
    
    frameFinal = np.zeros([36,32])
    for i in range(0,c.shape[0], 36):
        
        idct = fftpack.idct(c[i:i+36], type=4)
        frameFinal[:,int(i/36)] = idct/72
       
    return frameFinal

