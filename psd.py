from scipy import special
import numpy as np
import line_cod as cod
import matplotlib.pyplot as plt

def psd(codification, time):

    S = np.fft.fft(codification)/len(codification)
    x = np.fft.fftfreq(len(S), d = time[1] - time[0])
    S = S[1:int(len(S)/2)] # Plot only the positive values
    x = x[1:int(len(x)/2)] # Plot only the positive values
    
    return S, x

def qfunc(x):
    return 0.5*(1-special.erf(x))

def qinv(y):
    return np.sqrt(2)*special.erfinv(1-2*y)

def rcosfilter(N, beta, Ts, Fs):
    t = (np.arange(N) - N / 2)/Fs
    return np.where(np.abs(2*t) == Ts / beta,
        (np.pi / (4*Ts)) * np.sinc(1/2*beta),
        (1/Ts)*np.sinc(t/Ts) * np.cos(np.pi*beta*t/Ts) / (1 - (2*beta*t/Ts) ** 2))
