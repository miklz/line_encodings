import psd
import numpy as np
import line_cod as cod
import bit_rate_calc as br
import matplotlib.pyplot as plt

N = np.random.randint(32, 16000)
if N%2 != 0: N+=1

print(N)
bits = np.random.randint(2, size = N)

# Transmission and reception
line_freq, t = cod.rz_l(bits = bits, time_simb = 0.001, v_max = 5, v_min = -5)
x = br.bit_transmitter(line_freq, 0.001, 0.001, 0.5, 6, 20)
r = br.channel(x, 0.001, 30)
y = br.bit_receiver(r, 0.001, 0.001, 0.5, 6, 20)

plt.plot(x, 'y')
plt.plot(r, 'r')
plt.plot(y, 'g')
plt.show()

# Bit energy x Error 
#x = np.arange(0, 30, 0.1)
#EbpNo = 10**(x/10)
#y = psd.qfunc(np.sqrt(2*EbpNo))
#z = psd.qfunc(np.sqrt(EbpNo))
#plt.plot(x, y)
#plt.plot(x, z, 'r')
#plt.yscale('log')
#plt.show()

# Power spectral density of each codification 
#line_freq, t = cod.rz_l(bits = bits, time_simb = 0.001, v_max = 5, v_min = -5)
#X, s = psd.psd(line_freq, t)
#plt.plot(s, abs((X)))
#plt.show()

# Test to see the bit rate, variance and standard deviation of each
# codification
#rb, variance, des = br.calc_rate_simb(cod.manchester, bits, ts = 0.001, v_max = 5, v_min = 0)
#print(rb, variance, des)

# Testing each line codification
#vector, t = cod.nrz_l(bits, time_simb = 0.2, v_max = 5, v_min = -5)
#vector, t = cod.rz_l(bits = bits, time_simb = 0.001, v_max = 5, v_min = -5)
#vector, t = cod.quat_nrz(bits, time_simb = 1, v_max = 5, v_min = -5)
#vector, t = cod.nrz_s(bits, time_simb = 1, v_max = 5, v_min = 0)
#vector, t = cod.nrz_i(bits, time_simb = 0.001, v_max = 5, v_min = 0)
#vector, t = cod.manchester(bits, time_simb = 1, v_max = 5, v_min = 0)
#plt.plot(t, vector)
#plt.show()
