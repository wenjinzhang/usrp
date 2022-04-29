from unittest import result
import matplotlib.pyplot as plt

import numpy as np
base_signal = np.load('./signal_set_52subcarriers/base.npy')

subcarrier_map = {
  1: -26, 2: -25, 3: -24, 4: -23, 5: -22, 6: -21, 7: -20, 8: -19, 9: -18, 10: -17, 
  11: -16, 12: -15, 13: -14, 14: -13, 15: -12, 16: -11, 17: -10, 18: -9, 19: -8, 20: -7, 
  21: -6, 22: -5, 23: -4, 24: -3, 25: -2, 26: -1, 27: 1, 28: 2, 29: 3, 30: 4, 
  31: 5, 32: 6, 33: 7, 34: 8, 35: 9, 36: 10, 37: 11, 38: 12, 39: 13, 40: 14,
  41: 15, 42: 16, 43: 17, 44: 18, 45: 19, 46: 20, 47: 21, 48: 22, 49: 23, 50: 24, 
  51: 25, 52: 26
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
#   from scipy.fft import fft, fftfreq
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
        sine_wave = np.load('./signal_set_52subcarriers/sine_{}.npy'.format(abs(subcarrier_offset)))
        if subcarrier_offset > 0:
            result = result +  (config['v'] * base_signal + config['m']) * sine_wave 
        else:
            result = result +  (config['v'] * base_signal + config['m']) / sine_wave 

    

    return result

if __name__=='__main__':
    result = generate_attack_signal({
    1: {'v': 0.5, 'm': 0},
    3: {'v': 0.5, 'm': 0},
    4: {'v': 0.5, 'm': 0},
    8: {'v': 0.5, 'm': 0},
    13: {'v': 0.5, 'm': 0},
    16: {'v': 0.5, 'm': 0},
    25: {'v': 0.5, 'm': 0},
    30: {'v': 0.5, 'm':0},
    52: {'v': 0.5, 'm':0},
    })
    np.save('./data.npy', result)
    # plot_spec(result)
