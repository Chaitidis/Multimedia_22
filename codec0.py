import numpy as np
from scipy.io.wavfile import write
from matplotlib import pyplot as plt
import wave
import createFilters
import frame
import nothing
import mp3

def coder0(wavin, h, M, N):
    
    myfile = wave.open(wavin, 'r')
    
    nFrames = myfile.getnframes()
    
    
    for i in range(0,nFrames, M*N):
        myfile.setpos(i)
        samples = myfile.readframes(M*N)
        samples = np.frombuffer(samples, dtype=np.int16)
       
        samplesBuffer = np.concatenate((samples, np.zeros(h.shape[0]-M)), axis=0)
        frameFinal = frame.frame_sub_analysis(samplesBuffer, H=h, q=N)
        sameFrame = nothing.donothing(frameFinal)
        if i ==0:
            Ytot = sameFrame    
        else:
            Ytot = np.concatenate((Ytot, sameFrame), axis=0) 
    print(Ytot.shape)
    return Ytot

def decoder0(Ytot, h, M, N):
    for i in range(0, Ytot.shape[0], N):
        initFrame = Ytot[i:i+N,:]
        sameFrame = nothing.idonothing(initFrame)
        #ybuff = np.zeros((int(h.shape[0]/M), sameFrame.shape[1]))
        ybuff = np.concatenate((sameFrame,np.zeros((int(h.shape[0]/M)-1, sameFrame.shape[1]))), axis=0)
        frameFinal = frame.frame_sub_synthesis(ybuff, h)
        if i ==0:
            xhat = frameFinal
        else:
            xhat = np.concatenate((xhat,frameFinal),axis=0)    
    return xhat



def codec0(wavin, h, M, N):
    H = mp3.make_mp3_analysisfb(h,32)
    G = mp3.make_mp3_synthesisfb(h, 32)
    
    Ytot = coder0(wavin, H, M, N)
    xhat = decoder0(Ytot, G, M, N)
    
    return (xhat, Ytot)


xhat, Ytot = codec0('myfile.wav', createFilters.h, 32,36)

scaled = np.int16(xhat / np.max(np.abs(xhat)) * 32767)
write('myfile_hat.wav', 44100, scaled)
x = np.count_nonzero(xhat)
print(x)
# fig = plt.figure()
# ax = plt.axes()
# print(Ytot)

# ax.plot( xhat)
# plt.show()

