
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
import MP3cod

def MP3decod(final, h, M, N, SF, B):
    Ytot = []
    start = 0
    end = 1
    count = 1 + final[start,1]
    while count < M*N:
        count += 1 + final[end,1] 
        end += 1
    test1 = final[start: end]    
    symb_index = iRLE(final[start:end], K=N*M)
    DCT = all_bands_dequantizer(symb_index, B=B[0,:], SF=SF[0,:])
        
        
    
        #Ytot[k: k +N, :] = dct.iframeDCT(DCT[k*M: k*M +N*M])
    Ytot = something1.idosomething1(DCT)
    k = end
    i = N
    j = 1     
    while k <final.shape[0]:
        start = k
        end = k+1
        count = 1 + final[start,1]
        while count < M*N:
            count += 1 + final[end,1] 
            end += 1
        symb_index = iRLE(final[start: end], K=N*M)
        DCT = all_bands_dequantizer(symb_index, SF=SF[j,:], B=B[j,:])
        
        
    
        #Ytot[k: k +N, :] = dct.iframeDCT(DCT[k*M: k*M +N*M])
        Ytot = np.concatenate((Ytot,something1.idosomething1(DCT)), axis=0)
        j += 1
        i += N
        k += end - start 
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
     
         
    return (xhat,Ytot)

# h = np.load('h.npy', allow_pickle=True).tolist()['h'].reshape(-1,)
# G = mp3.make_mp3_synthesisfb(h, 32)
    
# xhat1,Ytot = MP3decod(MP3cod.rle, G, 32, 36, MP3cod.SF, MP3cod.B)

# scaled = np.int16(xhat1 / np.max(np.abs(xhat1)) * 32767)


# myfile = wave.open('myfile.wav', 'r')
# myfile_hat1 = wave.open('myfile_hat1.wav', 'wb')
# myfile_hat1.setnchannels(myfile.getnchannels())
# myfile_hat1.setsampwidth(myfile.getsampwidth())
# myfile_hat1.setframerate(myfile.getframerate())
# myfile_hat1.writeframesraw(scaled)

# samples = myfile.readframes(myfile.getnframes())
# x = np.frombuffer(samples, dtype=np.int16)