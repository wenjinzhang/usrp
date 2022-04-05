from unittest import result
import matplotlib.pyplot as plt
# from scipy.fft import fft, fftfreq
import numpy as np
base_signal = np.load('./signal_set/base.npy')

subcarrier_map = {
    1:-28,2:-26,3:-24,4:-22,5:-20,6:-18,7:-16,8:-14,9:-12,10:-10,
    11:-8,12:-6,13:-4, 14:-2, 15:-1, 16:1,17:3, 18:5, 19:7,20:9,
    21:11, 22:13, 23:15, 24:17,25:19,26:21,27:23,28:25,29:27,30:28,
}

# 'v' is variance;  'm' is mean
attack_configs = {
    1: {'v': 1, 'm': 0},
    5: {'v': 1, 'm': 0},
    7: {'v': 1, 'm': 0},
    10: {'v': 1, 'm': 0},
    28: {'v': 1, 'm': 0},
}

# check spec
# def plot_spec(y, sample_rate = 20e6):
#   yf = fft(y)
#   N = len(y)
#   xf = fftfreq(N, 1 / sample_rate)/1e6
#   plt.plot(xf, np.abs(yf))
#   plt.ylabel('Energy')
#   plt.xlabel('Frequency(MHz)')
#   plt.show()


def generate_attack_signal(attack_configs):
    result = np.zeros(np.shape(base_signal))
    for subidx in attack_configs:
        subcarrier_offset = subcarrier_map[subidx]
        config = attack_configs[subidx]
        sine_wave = np.load('./signal_set/sine_{}.npy'.format(abs(subcarrier_offset)))
        if subcarrier_offset > 0:
            result = result +  (config['v'] * base_signal + config['m']) * sine_wave 
        else:
            result = result +  (config['v'] * base_signal + config['m']) / sine_wave 

    

    return result

if __name__=='__main__':
    result = generate_attack_signal({
    16: {'v': 0.5, 'm': 0},
    
    })
    np.save('./data.npy', result)
    # plot_spec(result)
