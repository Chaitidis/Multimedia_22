import numpy as np
from matplotlib import pyplot as plt
import wave
import frame
import nothing
import mp3
import something1
import dct

def coder1(wavin, h, M, N):
    
    myfile = wave.open(wavin, 'r')
    nFrames = myfile.getnframes()
    
    for i in range(0,nFrames - M*N, M*N):
        myfile.setpos(i)
        samples = myfile.readframes(M*(N-1) + h.shape[0])
        samples = np.frombuffer(samples, dtype=np.int16)
        frameFinal = frame.frame_sub_analysis(samples, H=h, q=N)
        if i ==0:
            Ytest1 = frameFinal    
        else:
            Ytest1 = np.concatenate((Ytest1, frameFinal), axis=0)
        sameFrame = something1.dosomething1(frameFinal)
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
    
    Ytest1 = np.concatenate((Ytest1, frameFinal), axis=0)
    
    sameFrame = something1.dosomething1(frameFinal)
    DCT = np.concatenate((Ytot, sameFrame), axis=0)     
          
    return (DCT,Ytest1)

def decoder1(DCT, h, M, N):
    Ytot = np.zeros([int(DCT.shape[0]/M), M])
    for k in range(0, Ytot.shape[0], N):
        DCT1 = DCT[k: k +N*M]
        Ytot1 = Ytot[k: k +N, :] 
        Ytot2 = dct.iframeDCT(DCT[k: k +N*M])
        Ytot[k: k +N, :] = dct.iframeDCT(DCT[k*M: k*M +N*M])
        #Ytot[k: k +N, :] = something1.idosomething1(DCT[k: k +N*M])
        
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



def codec1(wavin, h, M, N):
   
    H = mp3.make_mp3_analysisfb(h,32)
    G = mp3.make_mp3_synthesisfb(h, 32)
    
    Ytot, Ytest1 = coder1(wavin, H, M, N)
    xhat,Ytest2 = decoder1(Ytot, G, M, N)
    
    return (xhat, Ytot,Ytest1,Ytest2)

h = np.load('h.npy', allow_pickle=True).tolist()['h'].reshape(-1,)

xhat, Ytot,Ytest1 ,Ytest2 = codec1('myfile.wav', h, 32,36)

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
# print("x",x[480:480+20] - np.round(xhat[0:20]))
# #print("xhat", xhat[0:20])
# print("x_pd",x_pd.shape)
# print("xhat_pd", xhat_pd.shape)
print(np.max(Ytest1-Ytest2))
snr = x_pd - xhat_pd
# delta = 10000
err = Ytest1 - Ytest2
ax.plot(snr)
# ax.plot(np.concatenate((np.zeros([36]), err[:,1]) ))
#ax.plot(Ytest1.T.reshape(16092,32)[:,1])
plt.show()

