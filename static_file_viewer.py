#!/usr/bin/env python

import numpy as np
import scipy.signal as ss
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from template_file_viewer import Ui_Form
import os, datetime

num_points = 0

UNIX_EPOCH = datetime.datetime(1970, 1, 1, 0, 0)

def now_timestamp(epoch=UNIX_EPOCH):
	return(int((datetime.datetime.now() - epoch).total_seconds()*1e6))

class QtPlotter:
	def __init__(self):
		self.app = QtGui.QApplication([])
		self.win = QtGui.QWidget()
		self.ui = Ui_Form()
		self.ui.setupUi(self.win)
		self.win.setWindowTitle('static file viewer')
		self.win.show()
		self.ui_plot = self.ui.plot
		self.plt = self.ui_plot.plot()
		# self.ui_plot.setRange(xRange=[-100, 100], yRange=[0, 2100])
		self.ui_plot.showGrid(x=True, y=True)
		# self.ui_plot.setTitle('start time '+datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S"))
		self.ui.loadDataBtn.clicked.connect(self.load_data)
		self.ui.windowLenSpin.valueChanged.connect(self.win_len_change)
		self.ui.winTypeComboBox.currentIndexChanged.connect(self.win_len_change)
		self.point_num = 0
		self.max_num_points = 50000
		self.data_x = []
		self.raw_data = np.zeros(self.max_num_points)
		self.sum_data = np.zeros((self.max_num_points, 16))
		# self.ui_plot.setAspectLocked(True)

	def load_data(self):
		filename = QtGui.QFileDialog.getOpenFileName(self.win, 'Open File', os.path.dirname(os.path.abspath(__file__)))
		data = np.load(str(filename))
		self.raw_data = data['count']
		self.x_time = []
		start_time = datetime.datetime.utcfromtimestamp(float(data['time'][0])/1e6)
		end_time = datetime.datetime.utcfromtimestamp(float(data['time'][1])/1e6)
		for i in xrange(len(data['count'])):
			x = start_time + datetime.timedelta(seconds=i)
			self.x_time.append(int((x - UNIX_EPOCH).total_seconds()*1e6))
		self.plt.setData(self.x_time, self.raw_data, pen='g')
		self.ui_plot.setTitle('start time '+start_time.strftime("%d.%m.%y %H:%M:%S")+'; end time '+end_time.strftime("%d.%m.%y %H:%M:%S"))

	def win_len_change(self):
		if str(self.ui.winTypeComboBox.currentText()) == 'rectangular':
			window = ss.boxcar(self.ui.windowLenSpin.value())
		elif str(self.ui.winTypeComboBox.currentText()) == 'tukey':
			window = ss.tukey(self.ui.windowLenSpin.value())
		elif str(self.ui.winTypeComboBox.currentText()) == 'hann':
			window = ss.hann(self.ui.windowLenSpin.value())
		data_conv = ss.convolve(self.raw_data, window, mode='same')
		self.plt.setData(self.x_time, data_conv, pen='g')

plotter = QtPlotter()


if __name__ == '__main__':
	import sys
	if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
		QtGui.QApplication.instance().exec_()
