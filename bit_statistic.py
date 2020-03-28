from scipy import special, signal
import numpy as np
import line_cod as cod
import matplotlib.pyplot as plt

def psd(codification, time):
    x, S = signal.welch(codification, 1/(time[1]-time[0]), nfft=5000)
    return S, x

def calc_rate_simb(codification, bits, ts, v_max, v_min):

    vector, _ = codification(bits = bits, time_simb = ts, v_max = v_max, v_min
            = v_min)
    
    rb = (1/ts)*np.log2(len(np.unique(vector, return_counts = True)))

    variance = np.var(vector)
    
    des = np.sqrt(variance)

    return rb, variance, des

def qfunc(x):
    return 0.5*(1-special.erf(x))

def qinv(y):
    return np.sqrt(2)*special.erfinv(1-2*y)
