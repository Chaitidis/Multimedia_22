import numpy as np
from matplotlib import pyplot as plt
from DCT_band_scale import DCT_band_scale
from quantizer import quantizer
from dequantizer import dequantizer
from critical_bands import critical_bands
from DCTpower import DCTpower
from Dksparse import Dksparse
from psycho import  psycho

def all_bands_quantizer(c: np.ndarray, Tg: np.ndarray) -> np.ndarray:

    bands = critical_bands(c.shape[0])
    cs, SF = DCT_band_scale(c)
    symb_index = np.zeros(c.shape[0])
    bits = np.zeros(SF.shape[0])
    
    for band in np.unique(bands):
        start = np.where(bands==band)[0][0]
        end = np.where(bands==band)[0][-1] + 1 
        b = 1
        test1 = cs*[bands == band][0]
        quant = quantizer(cs[start:end], b )
        cs_hat = dequantizer(np.int16(quant),b)
        band_c_hat = np.sign(cs_hat)*np.abs(cs_hat*SF[int(band-1)])**(4/3)
        error = np.abs(c[start:end] - band_c_hat)
        power = DCTpower(error)
        
        while np.array([(power - Tg[start:end]) > 0]).any():
            b += 1 
            quant = quantizer(cs[start:end], b )
            cs_hat = dequantizer(np.int16(quant),b)
            band_c_hat = np.sign(cs_hat)*np.abs(cs_hat*SF[int(band-1)])**(4/3)
            error = np.abs(c[start:end] - band_c_hat)
            power = DCTpower(error)
        bits[int(band)-1] = b
        symb_index[start:end] = quant 
        
    return (symb_index, SF, bits)    

np.random.seed(0)

data = np.random.uniform(-100,100, [1152])

Dk = Dksparse(1152)
Tq = np.array(np.load('Tq.npy', allow_pickle=True).tolist()[0])
Tg = psycho(data, Dk)
Tg1 = Tg -15
# Tg[1] = 68
# Tg[2] = 68
symb, scale, bit = all_bands_quantizer(data, Tg1)

# print(symb)

# fig = plt.figure()
# ax = plt.axes()
# ax.plot(symb)
# plt.show()