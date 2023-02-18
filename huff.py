import numpy as np
import RLE

def huff(run_symbols):
    # Convert RLE output to NumPy array
    rle_arr = np.array(run_symbols)

    # Compute symbol frequencies
    unique_symbols, indices = np.unique(rle_arr, axis=0, return_inverse=True)
    symbol_freqs = np.bincount(indices)
    symbol_rep = np.arange(unique_symbols.shape[0])
    # Build list of (frequency, symbol) tuples
    freq_symbol_list = [[symbol_rep[symbol], freq] for symbol, freq in enumerate(symbol_freqs) if freq > 0]

    class Nodes:
        def __init__(self, symbol, freq, parent=None, left=None, right=None, code=None):
            self.freq = freq
            self.symbol = symbol
            self.parent = parent
            self.left = left
            self.right = right
            self.code = code

    init_node_list = [Nodes(symbol_rep[symbol], freq) for symbol, freq in enumerate(symbol_freqs) if freq > 0]
    init_symbols = []
    init_freqs = []
    for symb in init_node_list:
        init_symbols.append(symb.symbol)
        init_freqs.append(symb.freq)
    init_symbols = np.array(init_symbols)
    init_freqs = np.array(init_freqs)
    node_list = init_node_list
    all_nodes = []
    
    node_list = sorted(node_list, key=lambda node: node.freq)
    # Build Huffman tree
    while len(node_list) > 1:
        # Find the two tuples with the lowest frequency
       
        min1 = node_list.pop(0)
        min_symbol1 = min1.symbol
        min_freq1 = min1.freq
        
        min2 = node_list.pop(0)
        min_symbol2 = min2.symbol
        min_freq2 = min2.freq
        
        
        new_freq = min_freq1 + min_freq2
        new_symbols = np.concatenate((min_symbol1.reshape(-1,), min_symbol2.reshape(-1,)), axis=0)
        new_node = Nodes(new_symbols,new_freq, left=min1, right= min2)
        min1.parent = new_node
        min1.code = '0'
        min2.parent = new_node
        min2.code = '1'
        node_list.append(new_node)
        all_nodes.append(min1)
        all_nodes.append(min2)
        all_nodes.append(new_node)

        # Sort the list by frequency in descending order
        node_list = sorted(node_list, key=lambda node: node.freq)
        
    codes_dict = ['' for i in range(len(init_symbols))]
    for node in all_nodes:
        if node.symbol in init_symbols and '' in codes_dict:
            code = node.code
            par = node.parent
            while par != None:
                if par.code != None:    
                    code += par.code
                par = par.parent
                   
            test1 = node.symbol
            if code != None:   
                codes_dict[np.argwhere(init_symbols == node.symbol)[0][0]] = code   

    
    # Encode RLE output using Huffman codes
    frame_stream = ''
    for i in rle_arr:
        
        frame_stream += codes_dict[symbol_rep[np.argwhere(unique_symbols == i)[0][0]]]
    
    # # Build numpy array of codes
    # codes = np.zeros((len(codes_dict), 3), dtype=np.float32)
    # for idx, (symbol, code) in enumerate(codes_dict.items()):
    #     codes[idx, 0] = symbol
    #     codes[idx, 1] = int(code, 2)
    #     codes[idx, 2] = symbol_freqs[symbol] / len(run_symbols)

    return frame_stream, codes

stream1, prob = huff(RLE.rle)

print(stream1)