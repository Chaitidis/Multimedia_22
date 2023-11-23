import numpy as np
from matplotlib import pyplot as plt
import frame
import mp3
from MP3cod import MP3cod
from MP3decod import MP3decod
import wave

def MP3codec(wavin, h, M, N):
   
    H = mp3.make_mp3_analysisfb(h,32)
    huff, rle, SF, B  = MP3cod(wavin, H, 32, 36)
    file = open("huff.txt", "w")
    file.write(huff)
    file.close()
    print("Encoded Signal Size: ", len(huff)/8, " bytes." )
    print("Encoding Complete. Decoding in progress...")
    
    G = mp3.make_mp3_synthesisfb(h, 32)
    xhat,Ytot = MP3decod(rle, G, 32, 36, SF, B)
    print("Decoding Complete!")
    return xhat

h = np.load('h.npy', allow_pickle=True).tolist()['h'].reshape(-1,)

xhat1 = MP3codec('myfile.wav', h, 32,36)

scaled = np.int16(xhat1 / np.max(np.abs(xhat1)) * 32767)


myfile = wave.open('myfile.wav', 'r')
myfile_hat1 = wave.open('myfile_hat1.wav', 'wb')
myfile_hat1.setnchannels(myfile.getnchannels())
myfile_hat1.setsampwidth(myfile.getsampwidth())
myfile_hat1.setframerate(myfile.getframerate())
myfile_hat1.writeframesraw(scaled)

samples = myfile.readframes(myfile.getnframes())
x = np.frombuffer(samples, dtype=np.int16)

fig = plt.figure()
ax = plt.axes()

x_pd = np.concatenate((x, np.zeros([480])), axis = 0)
xhat_pd = np.concatenate((np.zeros([480]), xhat1), axis=0)

file = open("huff.txt", "r")
data = file.read()

print( "Compression Ratio: ", 1029932/(len(data)/8))
print("Decoded signal SNR: ", 10*np.log10(np.var(xhat1)/np.var(x_pd-xhat_pd)))

ax.plot(x_pd - xhat_pd)
plt.show()