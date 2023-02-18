import numpy as np
from matplotlib import pyplot as plt
import all_bands_quantizer

def RLE(symb_index: np.ndarray, K: int) -> np.ndarray:
    # Initialize the first symbol and count
    current_symbol = symb_index[0]
    count = 0
    run_symbols = []

    # Iterate through the symb_index, starting at the second symbol
    for i in range(1, len(symb_index)):
        if symb_index[i] == 0:
            # If the current symbol is the same as the previous symbol, increment the count
            count += 1
        else:
            # If the current symbol is different from the previous symbol, add the previous symbol and count to the run_symbols and update the current symbol and count
            run_symbols.append([current_symbol, count])
            current_symbol = symb_index[i]
            count = 0

    # Add the final symbol and count to the run_symbols
    run_symbols.append([current_symbol, count])

    # Return the run_symbols as a numpy array
    return np.array(run_symbols)

rle = RLE(all_bands_quantizer.symb, all_bands_quantizer.symb.shape[0])

# print(rle)

# fig = plt.figure()
# ax = plt.axes()
# ax.plot(rle[:,1].T)
# plt.show()