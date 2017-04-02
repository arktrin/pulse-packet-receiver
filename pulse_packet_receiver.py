#!/usr/bin/env python

import numpy as np
# import scipy.signal as ss
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from template_packet_receiver import Ui_Form
from threading import Thread
import socket, struct, Queue, datetime

host = ''
port = 50987
data = np.zeros(100000)
pack_struct = '!' + 36*'B' + 2*'I'
count = 0
num_points = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind((host, port))

UNIX_EPOCH = datetime.datetime(1970, 1, 1, 0, 0)

def now_timestamp(epoch=UNIX_EPOCH):
	return(int((datetime.datetime.now() - epoch).total_seconds()*1e6))

class QtPlotter:
	def __init__(self):
		self.ports = []
		self.timer = pg.QtCore.QTimer()
		self.app = QtGui.QApplication([])
		self.win = QtGui.QWidget()
		self.ui = Ui_Form()
		self.ui.setupUi(self.win)
		self.win.setWindowTitle('live pulse counter')
		self.win.show()
		self.ui_plot = self.ui.plot
		# self.ui_plot.setRange(xRange=[-100, 100], yRange=[0, 2100])
		self.ui_plot.showGrid(x=True, y=True)
		self.ui_plot.setTitle('start time '+datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S"))
		self.ui.saveDataBtn.clicked.connect(self.save_data)
		self.ui.thresholdWriteBtn.clicked.connect(self.write_to_DAC)
		self.point_num = 0
		self.max_num_points = 50000
		self.data_x = []
		self.raw_data = np.zeros(self.max_num_points)
		self.sum_data = np.zeros((self.max_num_points, 16))
		self.start_time = now_timestamp()
		self.timer.timeout.connect(self.update)
		self.timer.start(0)
		# self.ui_plot.setAspectLocked(True)

	def getPort(self):
		q = Queue.Queue()
		plt = self.ui_plot.plot() # pen='g'
		self.ports.append((q, plt))
		return q

	def write_to_DAC(self):
		raw_value = self.ui.thresholdValueSpin.value()
		value = int((2**16-1)*raw_value/2500.0)
		value = value << 4
		packet = list(struct.unpack('4B', struct.pack('>I', value)))
		packet.pop(0)
		# print packet
		packet[0] += 48
		pack_values = [255, 170] + packet + 31*[0]
		packer = struct.Struct(len(pack_values)*'B')
		packed_data = packer.pack(*pack_values)
		sock.sendto(packed_data, ('192.168.2.255', port))

	def save_data(self):
		self.end_time = now_timestamp()
		start_end_time = np.array([self.start_time, self.end_time])
		start_time_str = datetime.datetime.utcfromtimestamp(float(self.start_time)/1e6).strftime("%d.%m.%y_%H-%M-%S")
		np.savez('saved_data/'+start_time_str+'.npz', time=start_end_time, count=self.raw_data[16:self.point_num+16])

	def update(self):
		for q, plt in self.ports:
			try:
				self.raw_data[self.point_num+16] = q.get(block=False)
				for i in xrange(16):
					self.sum_data[self.point_num, i] = np.sum(self.raw_data[self.point_num-i+16:self.point_num+17])
				# y,x = np.histogram(data, bins=np.linspace(-100,100,200))
				# plt.clear()
				x = now_timestamp()
				self.data_x.append(x)
				self.point_num += 1
				plt.setData(self.data_x, self.sum_data[:self.point_num, self.ui.windowLenSpin.value()-1], pen='g')
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
