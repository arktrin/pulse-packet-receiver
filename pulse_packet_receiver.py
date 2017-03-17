#!/usr/bin/env python

import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from template_packet_receiver import Ui_Form
from threading import Thread
import socket, struct, Queue

host = '192.168.2.103'
port = 50987
data = np.zeros(100000)
pack_struct = '!' + 36*'B' + 2*'I'
count = 0
num_points = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

class QtPlotter:

	def __init__(self):
		self.ports = []
		self.timer = pg.QtCore.QTimer()
		self.app = QtGui.QApplication([])
		self.win = QtGui.QWidget()
		self.ui = Ui_Form()
		self.ui.setupUi(self.win)
		self.win.show()
		self.ui_plot = self.ui.plot
		# self.ui_plot.setRange(xRange=[-100, 100], yRange=[0, 2100])
		self.ui_plot.showGrid(x=True, y=True)

		self.ui.saveDataBtn.clicked.connect(self.save_data)

		self.point_num = 0
		self.data = np.zeros(100000)

		self.timer.timeout.connect(self.update)
		self.timer.start(0)
		# self.ui_plot.setAspectLocked(True)

	def getPort(self):
		q = Queue.Queue()
		plt = self.ui_plot.plot() # pen='g'
		self.ports.append((q, plt))
		return q

	def save_data(self):
		print 'Hey!'

	def update(self):
		for q, plt in self.ports:
			try:
				self.data[self.point_num] = q.get(block=False)
				# y,x = np.histogram(data, bins=np.linspace(-100,100,200))
				# plt.clear()
				self.point_num += 1
				plt.setData(self.data[:self.point_num], pen='g')
			except Queue.Empty:
				pass

def qtLoop():
	import sys
	if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
		QtGui.QApplication.instance().exec_()

def main_loop():
	plotter = QtPlotter()
	curve = plotter.getPort()

	def producer():
		global sock,pack_struct,num_points
		while True:
			curve.put(( 10*np.random.randn()  ))
			data_raw, addr = sock.recvfrom(64)
			if len(data_raw) == 44:
				data_unpacked = struct.unpack(pack_struct, data_raw)
				data[num_points] = data_unpacked[-2] # - 1e5
				print data_unpacked[-2]
				num_points += 1

	p = Thread(target=producer)
	p.daemon = True
	p.start()
	qtLoop()

if __name__ == "__main__":
	main_loop()
