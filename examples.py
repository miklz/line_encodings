import psd
import numpy as np
import line_cod as cod
import bit_functions as bf
import matplotlib.pyplot as plt

#N = 20 #np.random.randint(32, 16000)
#if N%2 != 0: N+=1

#print(N)
#bits = np.random.randint(2, size = N)
#print(bits)
message = "hi"
print("message being send: ", message)
bits = bf.text_to_bits(message)
print(bits)
# Transmission and reception
line_freq, t = cod.nrz_i(bits = bits, time_simb = 1, v_max = 5, v_min = -5)
#plt.plot(t,line_freq)
x = bf.bit_transmitter(line_freq, 1, 0.001, 0.5, 6, 20)
r = bf.channel(x, 0.001, 10)
y = bf.bit_receiver(r, 1, 0.001, 0.5, 6, 20)
plt.plot(y)
plt.show()
bits_received = cod.demod_i(y, 0)
print(bits_received)
print("message received:", bf.text_from_bits(bits_received))

#print(bits)
print(bits_received)

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
