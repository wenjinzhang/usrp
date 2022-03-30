import uhd
import numpy as np
import time
from signal_generator import generate_attack_signal

usrp = uhd.usrp.MultiUSRP()
duration = 120 # seconds
center_freq = 5.2e9
sample_rate = 20e6
gain = 60 # [dB] start low then work your way up

signal = generate_attack_signal({
    4: {'v': 1, 'm': 0},
    5: {'v': 2, 'm': 0},
    7: {'v': 3, 'm': 0},
    10: {'v': 3, 'm': 0},
    27: {'v': 2, 'm': 0},
})

usrp.send_waveform(signal, duration, center_freq, sample_rate, [0], gain)