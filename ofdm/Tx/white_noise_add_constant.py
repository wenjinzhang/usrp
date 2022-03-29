#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: White Noise Add Constant
# GNU Radio version: 3.7.14.0
##################################################

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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
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


class white_noise_add_constant(gr.top_block, Qt.QWidget):

    def __init__(self, setgain=0.75):
        gr.top_block.__init__(self, "White Noise Add Constant")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("White Noise Add Constant")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "white_noise_add_constant")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 20e6
        self.noise_amp = noise_amp = 2
        self.lowcut = lowcut = 1
        self.highcut = highcut = 0.3125e6
        self.gain = gain = 0.95
        self.freq_usrp = freq_usrp = 5.2e9 + 0.3125e6 * 17
        self.const = const = 1

        self.gain = gain = setgain
        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(freq_usrp, 0)
        self.uhd_usrp_sink_0.set_normalized_gain(gain, 0)
        print("current gain is----->", gain, "bandwidth is", samp_rate)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win)

        self.qtgui_sink_x_0.enable_rf_freq(False)



        self.blocks_add_const_vxx_0 = blocks.add_const_vcc((const, ))
        self.band_pass_filter_0 = filter.fir_filter_ccf(1, firdes.band_pass(
        	1, samp_rate, lowcut, highcut, 1e6, firdes.WIN_KAISER, 6.76))
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, noise_amp, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.uhd_usrp_sink_0, 0))

        # close window timer
        self.timer = Qt.QTimer(self)
        self.timer.timeout.connect(self.close)
        self.timer.start(1000*(20-0.5))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "white_noise_add_constant")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.lowcut, self.highcut, 1e6, firdes.WIN_KAISER, 6.76))

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self.analog_noise_source_x_0.set_amplitude(self.noise_amp)

    def get_lowcut(self):
        return self.lowcut

    def set_lowcut(self, lowcut):
        self.lowcut = lowcut
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.lowcut, self.highcut, 1e6, firdes.WIN_KAISER, 6.76))

    def get_highcut(self):
        return self.highcut

    def set_highcut(self, highcut):
        self.highcut = highcut
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.lowcut, self.highcut, 1e6, firdes.WIN_KAISER, 6.76))

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.uhd_usrp_sink_0.set_normalized_gain(self.gain, 0)


    def get_freq_usrp(self):
        return self.freq_usrp

    def set_freq_usrp(self, freq_usrp):
        self.freq_usrp = freq_usrp
        self.uhd_usrp_sink_0.set_center_freq(self.freq_usrp, 0)

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const
        self.blocks_add_const_vxx_0.set_k((self.const, ))


def main(top_block_cls=white_noise_add_constant, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
