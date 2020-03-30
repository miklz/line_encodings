import numpy as np
import line_cod as cod
import bit_functions as bf
import bit_statistic as bs
import matplotlib.pyplot as plt

"""
# Testing each line codification
# Uncomment the line codification of interest to see the plot
bits = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0]
vector, t = cod.nrz_l(bits, time_simb = 0.2, v_max = 5, v_min = -5)
#vector, t = cod.rz_l(bits = bits, time_simb = 0.001, v_max = 5, v_min = -5)
#vector, t = cod.quat_nrz(bits, time_simb = 1, v_max = 5, v_min = -5)
#vector, t = cod.nrz_s(bits, time_simb = 1, v_max = 5, v_min = 0)
#vector, t = cod.nrz_i(bits, time_simb = 0.001, v_max = 5, v_min = 0)
#vector, t = cod.manchester(bits, time_simb = 1, v_max = 5, v_min = 0)
plt.plot(t, vector)
plt.show()
"""

"""
# Test to see the bit rate, variance and standard deviation for a given
# codification
rb, variance, des = br.calc_rate_simb(cod.manchester, bits, ts = 0.001, v_max = 5, v_min = 0)
print(rb, variance, des)
"""

"""
N = np.random.randint(32, 16000)
if N%2 != 0: N+=1 ## making sure the number of bits it's even, this is only required to the polar quaternary line encode
bits = np.random.randint(2, size = N)


# Power spectral density
# Substitute the line codification to see the energy occupied in each lobe
line_freq, t = cod.rz_l(bits = bits, time_simb = 0.001, v_max = 5, v_min = 0)
X, s = bs.psd(line_freq, t)
plt.plot(s, X)
vector, t = cod.nrz_l(bits, time_simb = 0.001, v_max = 5, v_min = 0)
X, s = bs.psd(vector, t)
plt.plot(s, X, 'r')
#vector, t = cod.quat_nrz(bits, time_simb = 1, v_max = 5, v_min = -5)
#vector, t = cod.nrz_s(bits, time_simb = 0.001, v_max = 5, v_min = 0)
#X, s = bs.psd(vector, t)
#plt.plot(s, X, 'y')
#vector, t = cod.nrz_i(bits, time_simb = 0.001, v_max = 5, v_min = 0)
#plt.plot(s, X, 'm')
vector, t = cod.manchester(bits, time_simb = 0.001, v_max = 5, v_min = 0)
X, s = bs.psd(vector, t)
plt.plot(s, X, 'g')
plt.xlim(0, 2000)
plt.show()
"""

"""
# Bit energy x Error
# This block will plot a log graph comparing the energy by bit versus the error
# produced when this energy is increased or decreased
x = np.arange(0, 30, 0.1)
EbpNo = 10**(x/10)
y = bs.qfunc(np.sqrt(2*EbpNo))
z = bs.qfunc(np.sqrt(EbpNo))
plt.plot(x, y)
plt.plot(x, z, 'r')
plt.yscale('log')
plt.show()
"""

message = "Let's see how many characters are wrong in this text"
print("message being send: ", message)
bits = bf.text_to_bits(message)
# Add sincronization bits at the beginning and the end
sinc = [1, 0, 0, 0, 0, 0, 0, 1]
bits = sinc+bits+sinc
# Transmission and reception
line_freq, t = cod.nrz_l(bits = bits, time_simb = 1, v_max = 5, v_min = -5)
x = bf.bit_transmitter(line_freq, 1, 0.001, 0.5, 6, 20)
r = bf.channel(x, 1, 0)
y = bf.bit_receiver(r, 1, 0.001, 0.5, 6, 20)
plt.plot(y)
plt.show()
bits_received = cod.demod_l(y, 0)
print("message received:", bf.text_from_bits(bits_received))
