#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# arrange attack_gui

##################################################
from attack_gui import attack_gui
if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
import time
from gnuradio import qtgui
import threading
import time
start_time = time.time()

gains = [0.5, 0.55, 0.6, 0.65, 0.70, 0.75, 0.8]
data_rate = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1 ]
variances = [0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6]


def main(top_block_cls=attack_gui, options=None):
    global start_time

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(0)
    
    while True:
        if time.time()-start_time >= 10:
            break
        time.sleep(1)

    
    for i in range(3):
            print('time:', time.time()-start_time)
            tb = top_block_cls(setgain=gains[i], data_rate=1, var=0.5)
            tb.start()
            tb.show()
            def quitting():
                tb.stop()
                tb.wait()
            qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
            # qapp.exec_()
            qapp.exec_()
     

if __name__ == '__main__':
    # print(attack_gui.gain)
    main()