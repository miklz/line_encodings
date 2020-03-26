import psd
import numpy as np
from scipy.signal import upfirdn

def calc_rate_simb(codification, bits, ts, v_max, v_min):

    vector, _ = codification(bits = bits, time_simb = ts, v_max = v_max, v_min
            = v_min)
    
    rb = (1/ts)*np.log2(len(np.unique(vector, return_counts = True)))

    variance = np.var(vector)
    
    des = np.sqrt(variance)

    return rb, variance, des

def bit_transmitter(bits, Tb, Eb, alfa, span, sps):
    A = np.sqrt(Eb/Tb)

    c = psd.rcosfilter(len(bits), alfa, span, sps)
    s = upfirdn(A*np.sqrt(Tb)*c, bits, up = sps)

    return s

def channel(signal, Eb, EbNodb):
    EbNo = 10**(EbNodb/10)
    No = Eb/EbNo
    sigma = np.sqrt(No/2)

    r = signal + sigma*np.random.random(len(signal))

    return r

def bit_receiver(signal, Tb, Eb, alfa, span, sps):
    A = np.sqrt(Eb/Tb)

    c = psd.rcosfilter(len(signal), alfa, span, sps)
    y = upfirdn(A*np.sqrt(Tb)*c, signal, down = sps)

    # Keeping only the signal
    for x in range(len(y)):
        if abs(y[x]) > 0.005:
            break

    y = y[x:len(y)-x]

    return y

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    bits = bits.zfill(8 * ((len(bits) + 7) // 8))
    bits = [int(s) for s in bits]
    return bits

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    bits = map(str, bits)
    bits = ''.join(bits)
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
