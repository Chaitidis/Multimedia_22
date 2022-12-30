import numpy as np
from matplotlib import pyplot as plt
import mp3

h = np.load('h.npy', allow_pickle=True).tolist()['h'].reshape(-1,)
H = mp3.make_mp3_analysisfb(h, 32)

H = np.array(H)




fig1 = plt.figure()
ax1 = plt.axes()

hz = np.linspace(-44100, 44100, 512)

for i in range(H.shape[1]):
    ax1.plot(hz, 10*np.log10(np.fft.fft(H[:,i])))
plt.show()

fig2 = plt.figure()
ax2 = plt.axes()

barks = 13*np.arctan(0.00076*hz) + 3.5*np.arctan((hz/7500)**2)

for i in range(H.shape[1]):
    ax2.plot(barks, 10*np.log10(np.fft.fft(H[:,i])))
plt.show()