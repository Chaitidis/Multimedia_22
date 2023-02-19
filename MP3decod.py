
import numpy as np
from matplotlib import pyplot as plt
import wave
import frame
import nothing
import mp3
import something1
import dct
from all_bands_quantizer import all_bands_quantizer
from RLE import RLE
from huff import huff
from iRLE import iRLE
from dequantizer import dequantizer
from all_bands_dequantizer import all_bands_dequantizer

def MP3decod(final, h, M, N, SF, B):
    Ytot = np.zeros([int(final.shape[0]/M), M])
    for k in range(0, final.shape[0], N*M):
        symb_index = iRLE(final[k:k + M*N], K=N*M)
        DCT = all_bands_dequantizer(symb_index, SF=SF[:,k], B=B[:,k])
        
        
    
        #Ytot[k: k +N, :] = dct.iframeDCT(DCT[k*M: k*M +N*M])
        Ytot[k: k +N, :] = something1.idosomething1(DCT)
        
    for i in range(0, Ytot.shape[0]-N, N):
        ybuff = Ytot[i:i+(N)+int(h.shape[0]/M),:]
        frameFinal = frame.frame_sub_synthesis(ybuff, h)
        
        if i ==0:
            xhat = frameFinal
        else:
            xhat = np.concatenate((xhat,frameFinal),axis=0) 
            
    i = Ytot.shape[0] - N
    initFrame = Ytot[i:i+N, :]    
    padding = np.zeros((int(h.shape[0]/M), initFrame.shape[1]))
    ybuff = np.concatenate((initFrame,padding), axis=0)
    frameFinal = frame.frame_sub_synthesis(ybuff, h)
    xhat = np.concatenate((xhat,frameFinal),axis=0)    
    print(xhat.shape) 
         
    return (xhat,Ytot)