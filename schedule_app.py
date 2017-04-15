#!/usr/bin/env python

from PyQt4 import QtGui
import sys, os, subprocess
import template_schedule

class ScheduleApp(QtGui.QMainWindow, template_schedule.Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)  
		self.tableWidget.setColumnWidth(2, 160)
		self.addTaskBtn.clicked.connect(self.add_task)

	def add_task(self):
		start = str(self.startTimeEdit.text()).strip()
		end = str(self.endTimeEdit.text()).strip()
		threshold = str(self.thresholdValSpin.value())
		text_for_at = ' '.join(start[:-3].split(' ')[::-1])
		bash_command = 'echo "env DISPLAY=:0 pulse_packet_receiver.py" '+start+' '+end+' '+threshold+' | at '+text_for_at
		process = subprocess.Popen(['bash','-c', bash_command], stdout=subprocess.PIPE)
		output, error = process.communicate()
		print output, error


def main():
	app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
	form = ScheduleApp()
	form.show()  # Show the form
	app.exec_()  # and execute the app


if __name__ == '__main__':
	main()  # run the main function
