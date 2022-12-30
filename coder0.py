import numpy as np
from matplotlib import pyplot as plt
import wave
import createFilters

def coder0(wavin, h, M, N):
    
    myfile = wave.open(wavin, 'r')
    myfile.setpos(M*N)
    frames = myfile.readframes(M*N)
    frames_array = np.frombuffer(frames, dtype=np.int16)
    print(myfile.getnframes())
    return frames_array

Ytot = coder0('myfile.wav', createFilters.h, 32, 36)

fig = plt.figure()
ax = plt.axes()
#print(Ytot)
ax.plot(Ytot)
plt.show()