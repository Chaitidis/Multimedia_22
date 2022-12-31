import numpy as np
from matplotlib import pyplot as plt
import wave
import createFilters
import frame

def coder0(wavin, h, M, N):
    
    myfile = wave.open(wavin, 'r')
    
    nFrames = myfile.getnframes()
    
    for i in range(0,nFrames, M*N):
        myfile.setpos(i)
        samples = myfile.readframes(M*N)
        samples = np.frombuffer(samples, dtype=np.int16)
        frameFinal = frame.frame_sub_analysis(samples, H=h, q=3)
        
    return frameFinal

Ytot = coder0('myfile.wav', createFilters.H, 32, 36)

fig = plt.figure()
ax = plt.axes()
print(Ytot)
for k in range(Ytot.shape[0]):
    ax.plot(np.arange(Ytot.shape[1]-1), Ytot[k,1:])
plt.show()