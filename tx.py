import uhd
import numpy as np
import time
from signal_generator import generate_attack_signal

usrp = uhd.usrp.MultiUSRP()
duration = 120 # seconds
center_freq = 5.2e9
sample_rate = 20e6
gain = 0.7 # [dB] start low then work your way up

signal = generate_attack_signal({
    16: {'v': 1, 'm': 0},
})

usrp.send_waveform(signal, duration, center_freq, sample_rate, [0], gain*90)