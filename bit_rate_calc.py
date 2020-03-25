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
    s = upfirdn(A*np.sqrt(Tb)*c, bits, down = sps)

    return s

def channel(signal, Eb, EbNodb):
    EbNo = 10**(EbNodb/10)
    No = Eb/EbNo
    sigma = np.sqrt(No/2)

    r = signal + sigma*np.random.random(len(signal))
    print("r", len(r))

    return r

def bit_receiver(signal, Tb, Eb, alfa, span, sps):
    A = np.sqrt(Eb/Tb)

    c = psd.rcosfilter(len(signal), alfa, span, sps)
    y = upfirdn(A*np.sqrt(Tb)*c, signal, up = sps)
    print("y:", len(y))

    return y

def demodulator(signal, Tb, threshold):
    bits = np.zeros(len(signal), dtype = int)
    time_ref = np.linspace(0, len(signal), len(signal)) 

    j = 0
    index = 0
    time_s = 1120
    while j < len(signal):
        if  abs(signal[j]) > 0.005:
            if signal[j] > threshold:
                bits[index] = 1
            else: bits[index] = 0
        
            if time_ref[j] > time_s:
                time_s += 102
                index += 1
        j+=1

    return bits
