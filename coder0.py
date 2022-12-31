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
        samples = np.frombuffer(frame, dtype=np.int16)
        frameFinal = frame.frame_sub_analysis(samples, h, N)
    return frame

Ytot = coder0('myfile.wav', createFilters.h, 32, 36)

fig = plt.figure()
ax = plt.axes()
#print(Ytot)
ax.plot(Ytot)
plt.show()