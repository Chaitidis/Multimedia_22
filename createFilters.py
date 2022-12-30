import numpy as np
from matplotlib import pyplot as plt
import mp3

h = np.load('h.npy', allow_pickle=True).tolist()['h'].reshape(-1,)

H = mp3.make_mp3_analysisfb(h, 32)
G = mp3.make_mp3_synthesisfb(h, 32)

H = np.array(H)
G = np.array(G)

fig, ax = plt.subplots(3,1)
plt.subplots_adjust(right=0.975, wspace=0.2, hspace=0.869)

hz = np.linspace(-44100, 44100, 512)
barks = 13*np.arctan(0.00076*hz) + 3.5*np.arctan((hz/7500)**2)

for i in range(H.shape[1]):
    ax[0].plot(hz, 10*np.log10(np.fft.fft(H[:,i])))

for i in range(H.shape[1]):
    ax[1].plot(barks, 10*np.log10(np.fft.fft(H[:,i])))


ax[2].plot(hz , barks)

ax[0].set_ylabel("dB")
ax[1].set_ylabel("dB")
ax[2].set_ylabel("Barks")

ax[0].set_xlabel("Hz")
ax[0].set_xlabel("Barks")
ax[0].set_xlabel("Hz")

ax[0].set_title("Subband Filters in Hz", fontweight='bold')
ax[1].set_title("Subband Filters in Barks", fontweight='bold')
ax[2].set_title("Hz to Barks", fontweight='bold')

plt.show()