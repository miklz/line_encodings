import numpy as np

def nrz_l(bits, time_simb, v_max, v_min):
    vector = np.array(bits)
    new_vector = np.arange(0, len(bits)*time_simb, time_simb/100)
    shift_time = np.linspace(0, len(bits)*time_simb, len(new_vector))
    time_p = time_simb 
    index = 0
    j = 0
    while j < len(new_vector):
        if vector[index] == 1: 
            new_vector[j] = v_max 
        else: 
            new_vector[j] = v_min 
        if shift_time[j] > time_p:
            time_p += time_simb
            index += 1
        j += 1
    return new_vector, shift_time

def nrz_s(bits, time_simb, v_max, v_min):
    vector = np.array(bits)
    new_vector = np.arange(0, len(bits)*time_simb, time_simb/100)
    shift_time = np.linspace(0, len(bits)*time_simb, len(new_vector))
    time_p = time_simb
    new_vector[0] = v_min
    index = 0
    j = 1
    while j < len(new_vector):
        new_vector[j] = new_vector[j-1]
        if shift_time[j] > time_p:
            time_p += time_simb
            index += 1
            if vector[index] == 0:
                if new_vector[j-1] == v_max: new_vector[j] = v_min
                else: new_vector[j] = v_max
        j += 1
    return new_vector, shift_time

def nrz_i(bits, time_simb, v_max, v_min):
    vector = np.array(bits)
    new_vector = np.arange(0, len(bits)*time_simb, time_simb/100)
    shift_time = np.linspace(0, len(bits)*time_simb, len(new_vector))
    time_p = time_simb
    new_vector[0] = v_min
    index = 0
    j = 1
    while j < len(new_vector):
        new_vector[j] = new_vector[j-1]
        if shift_time[j] > time_p:
            time_p += time_simb
            index += 1
            if vector[index] == 1:
                if new_vector[j-1] == v_max: new_vector[j] = v_min
                else: new_vector[j] = v_max
        j += 1
    return new_vector, shift_time

def rz_l(bits, time_simb, v_max, v_min, time_ret=0.2):
    vector = np.array(bits)
    new_vector = np.arange(0, len(bits)*time_simb, time_simb/100)
    shift_time = np.linspace(0, len(bits)*time_simb, len(new_vector))
    time_p = time_simb
    index = 0
    j = 0

    while j < len(new_vector):
        if vector[index] == 1: 
            new_vector[j] = v_max 
        else: 
            new_vector[j] = v_min
        if shift_time[j] > time_p - time_simb*time_ret: new_vector[j] = 0
        if shift_time[j] > time_p: 
            time_p += time_simb
            index += 1
        j += 1

    return new_vector, shift_time

def quat_nrz(bits, time_simb, v_max, v_min):
    vector = np.array(bits)
    new_vector = np.arange(0, len(bits)*time_simb, time_simb/100)
    shift_time = np.linspace(0, len(bits)*time_simb/2, len(new_vector))
    time_p = time_simb
    index = 0
    j = 0
    while j < len(new_vector):
        if vector[index] == 0 and vector[index + 1] == 0: new_vector[j] = v_min
        elif vector[index] == 1 and vector[index + 1] == 0: new_vector[j] = v_min/2
        elif vector[index] == 0 and vector[index + 1] == 1: new_vector[j] = v_max/2
        elif vector[index] == 1 and vector[index + 1] == 1: new_vector[j] = v_max

        if shift_time[j] > time_p: 
            time_p += time_simb
            index += 2
        j += 1

    return new_vector, shift_time

def manchester(bits, time_simb, v_max, v_min):
    vector = np.array(bits)
    new_vector = np.arange(0, len(bits)*time_simb, time_simb/100)
    shift_time = np.linspace(0, len(bits)*time_simb, len(new_vector))
    time_p = time_simb
    index = 0
    j = 0
    while j < len(new_vector):
        if shift_time[j] <= time_p - time_simb/2:
            if vector[index] == 0: new_vector[j] = v_max
            else: new_vector[j] = v_min
        elif shift_time[j] <= time_p:
            if vector[index] == 0: new_vector[j] = v_min
            else: new_vector[j] = v_max
        else:
            new_vector[j] = new_vector[j-1]
            time_p += time_simb
            index += 1 
        j += 1
    
    return new_vector, shift_time

def demod_l(signal, threshold):
    bits = np.zeros(int(len(signal)/100)+1, dtype = int)
    time_ref = np.linspace(0, len(signal), len(signal)) 

    j = 0
    index = 0
    time_s = 50
    while j < len(signal):
        if signal[j] > threshold:
            bits[index] = 1
        else: bits[index] = 0
        
        if time_ref[j] > time_s:
            time_s += 100
            index += 1
        j+=1

    return bits[:-1]

def demod_s(signal, threshold): 
    bits_l = demod_l(signal, threshold)
    bits = np.zeros(len(bits_l), dtype = int)
    bits[0] = bits_zl[0]
    
    j = 1
    while j < len(bits_zl):
        if bits_l[j] != bits_l[j-1]:
            bits[j] = 0
        else: bits[j] = 1

        j+=1

    return bits

def demod_i(signal, threshold): 
    bits_l = demod_l(signal, threshold)
    bits = np.zeros(len(bits_l), dtype = int)
    bits[0] = bits_l[0]
    
    j = 1
    while j < len(bits_l):
        if bits_l[j] != bits_l[j-1]:
            bits[j] = 1
        else: bits[j] = 0

        j+=1

    return bits
