import numpy as np
from matplotlib import pyplot as plt
import frame
import mp3
from MP3cod import MP3cod
from MP3decod import MP3decod
import wave

def MP3codec(wavin, h, M, N):
   
    H = mp3.make_mp3_analysisfb(h,32)
    G = mp3.make_mp3_synthesisfb(h, 32)
    
    huff, rle, SF, B  = MP3cod(wavin, H, M, N)
    xhat,Ytot = MP3decod(rle, G, M, N, SF, B)
    
    
    return xhat

h = np.load('h.npy', allow_pickle=True).tolist()['h'].reshape(-1,)

xhat1 = MP3codec('myfile.wav', h, 32,36)

scaled = np.int16(xhat1 / np.max(np.abs(xhat1)) * 32767)


myfile = wave.open('myfile.wav', 'r')
myfile_hat = wave.open('myfile_hat.wav', 'wb')
myfile_hat.setnchannels(myfile.getnchannels())
myfile_hat.setsampwidth(myfile.getsampwidth())
myfile_hat.setframerate(myfile.getframerate())
myfile_hat.writeframesraw(scaled)

samples = myfile.readframes(myfile.getnframes())
x = np.frombuffer(samples, dtype=np.int16)