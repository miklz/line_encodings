import numpy as np
from scipy.signal import upfirdn

def rcosfilter(N, beta, Ts, Fs):
    t = (np.arange(N) - N / 2)/Fs
    existing = np.seterr(divide="ignore")
    c_filter = np.where(np.abs(2*t) == Ts / beta,
        (np.pi / (4*Ts)) * np.sinc(1/2*beta),
        (1/Ts)*np.sinc(t/Ts) * np.cos(np.pi*beta*t/Ts) / (1 - (2*beta*t/Ts) ** 2))
    np.seterr(**existing)
    return c_filter

def bit_transmitter(bits, Tb, Eb, alfa, span, sps):
    A = np.sqrt(Eb/Tb)
    c = rcosfilter(len(bits), alfa, span, sps)
    s = upfirdn(A*np.sqrt(Tb)*c, bits, up = sps)

    return s

def channel(signal, Eb, EbNodb):
    EbNo = 10**(EbNodb/10)
    No = Eb/EbNo
    sigma = np.sqrt(No/2)

    r = signal + sigma*(2*np.random.random(len(signal)) - 1)
    
    return r

def bit_receiver(signal, Tb, Eb, alfa, span, sps):
    A = np.sqrt(Eb/Tb)
    c = rcosfilter(len(signal), alfa, span, sps)
    y = upfirdn(A*np.sqrt(Tb)*c, signal, down = sps)

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
