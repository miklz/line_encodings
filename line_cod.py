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
