import numpy as np
from matplotlib import pyplot as plt
import wave
import frame
import nothing
import mp3
import dct

def coder0(wavin, h, M, N):
    
    myfile = wave.open(wavin, 'r')
    nFrames = myfile.getnframes()
    
    for i in range(0,nFrames - M*N, M*N):
        myfile.setpos(i)
        samples = myfile.readframes(M*(N-1) + h.shape[0])
        samples = np.frombuffer(samples, dtype=np.int16)
        frameFinal = frame.frame_sub_analysis(samples, H=h, q=N)
        sameFrame = nothing.donothing(frameFinal)
        if i ==0:
            Ytot = sameFrame    
        else:
            Ytot = np.concatenate((Ytot, sameFrame), axis=0)
                
    i = nFrames - M*N
    myfile.setpos(i)
    samples = myfile.readframes(M*N)
    samples = np.frombuffer(samples, dtype=np.int16)
    padding = np.zeros(h.shape[0])
    samples = np.concatenate((samples, padding), axis=0)
    frameFinal = frame.frame_sub_analysis(samples, H=h, q=N)
    sameFrame = nothing.donothing(frameFinal)
    Ytot = np.concatenate((Ytot, sameFrame), axis=0)     
          
    return Ytot

def decoder0(Ytot, h, M, N):
    
    for k in range(0, Ytot.shape[0], N):
        Ytot[k: k +N, :] = nothing.idonothing(Ytot[k: k +N, :])
        
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
          
    return xhat



def codec0(wavin, h, M, N):
   
    H = mp3.make_mp3_analysisfb(h,32)
    G = mp3.make_mp3_synthesisfb(h, 32)
    
    Ytot = coder0(wavin, H, M, N)
    xhat = decoder0(Ytot, G, M, N)
    
    return (xhat, Ytot)

h = np.load('h.npy', allow_pickle=True).tolist()['h'].reshape(-1,)

xhat, Ytot = codec0('myfile.wav', h, 32,36)

scaled = np.int16(xhat / np.max(np.abs(xhat)) * 32767)


myfile = wave.open('myfile.wav', 'r')
myfile_hat = wave.open('myfile_hat.wav', 'wb')
myfile_hat.setnchannels(myfile.getnchannels())
myfile_hat.setsampwidth(myfile.getsampwidth())
myfile_hat.setframerate(myfile.getframerate())
myfile_hat.writeframesraw(scaled)

samples = myfile.readframes(myfile.getnframes())
x = np.frombuffer(samples, dtype=np.int16)



fig = plt.figure()
ax = plt.axes()

x_pd = np.concatenate((x, np.zeros([480])), axis = 0)
xhat_pd = np.concatenate((np.zeros([480]), xhat), axis=0)

snr = x_pd - xhat_pd



ax.plot(snr )
plt.show()

