import numpy as np
from matplotlib import pyplot as plt
import wave
import frame
import nothing
import mp3
import something1
import dct
from all_bands_quantizer import all_bands_quantizer
from RLE import RLE
from huff import huff


def MP3cod(wavin, h, M, N):
    
    myfile = wave.open(wavin, 'r')
    nFrames = myfile.getnframes()
    Tq = np.array(np.load('Tq.npy', allow_pickle=True).tolist()[0]) 
    
    scale = np.ndarray([int(nFrames/(M*N)),25])
    bits = np.ndarray([int(nFrames/(M*N)),25])
    
    for i in range(0,nFrames - M*N, M*N):
        myfile.setpos(i)
        samples = myfile.readframes(M*(N-1) + h.shape[0])
        samples = np.frombuffer(samples, dtype=np.int16)
        frameFinal = frame.frame_sub_analysis(samples, H=h, q=N)
        # if i ==0:
        #     Ytest1 = frameFinal    
        # else:
        #     Ytest1 = np.concatenate((Ytest1, frameFinal), axis=0)
        DCTframe, Tg = something1.dosomething1(frameFinal)
        quantFrame, scale[int(i/(M*N)),:], bits[int(i/(M*N)),:] = all_bands_quantizer(DCTframe, Tg)
        RLEframe = RLE(quantFrame,1152)
        
        frame_stream, frame_symbol_prob = huff(RLEframe)
        if i ==0:
            final = frame_stream
            final_1 = RLEframe
            # ax.plot(Tq)
            # ax.plot(Tg - 30)    
        else:
            final += frame_stream
            final_1 = np.concatenate((final_1, RLEframe), axis=0)
            # ax.plot(Tq)
            # ax.plot(Tg - 30)  
               
    i = nFrames - M*N
    myfile.setpos(i)
    samples = myfile.readframes(M*N)
    samples = np.frombuffer(samples, dtype=np.int16)
    padding = np.zeros(h.shape[0])
    samples = np.concatenate((samples, padding), axis=0)
    frameFinal = frame.frame_sub_analysis(samples, H=h, q=N)
    
    #Ytest1 = np.concatenate((Ytest1, frameFinal), axis=0)
    
    DCTframe, Tg = something1.dosomething1(frameFinal)
    quantFrame, scale[int(i/(M*N)),:], bits[int(i/(M*N)),:] = all_bands_quantizer(DCTframe, Tg)
    RLEframe = RLE(quantFrame,1152)
    frame_stream, frame_symbol_prob = huff(RLEframe)
    final_1 = np.concatenate((final_1, RLEframe), axis=0)
    final += frame_stream    
          
    return (final, final_1, scale, bits)

# h = np.load('h.npy', allow_pickle=True).tolist()['h'].reshape(-1,)
# H = mp3.make_mp3_analysisfb(h,32)
# huff, rle, SF, B  = MP3cod('myfile.wav', H, 32, 36)