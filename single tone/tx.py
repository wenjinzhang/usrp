import uhd
import numpy as np
import time

usrp = uhd.usrp.MultiUSRP()
samples = 0.1*np.random.randn(10000) + 0.1j*np.random.randn(10000) # create random signal
duration = 60 # seconds
center_freq = 5e9 - 312500*10 

sample_rate = 1e6
gain = 60 # [dB] start low then work your way up
start_time = time.time()

# time.sleep(40)

norm_gains = [0.80, 0.90, 1]
gains = [x*90 for x in norm_gains]
for gain in gains:
    print("--------start to send:{}---------------------------".format(time.time()-start_time))
    usrp.send_waveform(samples, duration, center_freq, sample_rate, [0], gain)
    print("---------sent at {} gain-------------".format(gain))