#!/usr/bin/env python

from PyQt4 import QtGui, QtCore
import sys, os, datetime
import subprocess as sp
import template_schedule

now = datetime.datetime.now()
soon = now + datetime.timedelta(minutes=1)
then = now + datetime.timedelta(minutes=2)

class ScheduleApp(QtGui.QMainWindow, template_schedule.Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)  
		# self.tableWidget.setColumnWidth(2, 160)
		header = self.tableWidget.horizontalHeader()
		header.setResizeMode(QtGui.QHeaderView.Stretch)
		self.startDateTimeEdit.setDate(QtCore.QDate(soon.year, soon.month, soon.day))
		self.startDateTimeEdit.setTime(QtCore.QTime(soon.hour, soon.minute, soon.second))
		self.endDateTimeEdit.setDate(QtCore.QDate(then.year, then.month, then.day))
		self.endDateTimeEdit.setTime(QtCore.QTime(then.hour, then.minute, then.second))
		self.startDateTimeEdit.setMaximumDate(QtCore.QDate(2030, 12, 31))
		self.startDateTimeEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(now.year, now.month, now.day), QtCore.QTime(now.hour, now.minute, now.second)))
		self.endDateTimeEdit.setMaximumDate(QtCore.QDate(2030, 12, 31))
		self.endDateTimeEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(now.year, now.month, now.day), QtCore.QTime(now.hour, now.minute, now.second)))
		self.addTaskBtn.clicked.connect(self.add_task)

	def add_task(self):
		start = self.startDateTimeEdit.dateTime().toPyDateTime().strftime("%d.%m.%y %H:%M")
		end = self.endDateTimeEdit.dateTime().toPyDateTime().strftime("%d.%m.%y %H:%M:%S")
		threshold = str(self.thresholdValSpin.value())
		text_for_at = self.startDateTimeEdit.dateTime().toPyDateTime().strftime("%H:%M %d.%m.%y")
		bash_command = 'echo "env DISPLAY=:0 pulse_packet_receiver.py" '+start+' '+end+' '+threshold+' | at '+text_for_at
		process = sp.Popen(['bash','-c', bash_command], stdout=sp.PIPE)
		output, error = process.communicate()
		print output.read()
		if error == None:
			rowPosition = self.tableWidget.rowCount()
			self.tableWidget.insertRow(rowPosition)
			self.tableWidget.setItem(rowPosition , 0, QtGui.QTableWidgetItem(start+':00'))
			self.tableWidget.setItem(rowPosition , 1, QtGui.QTableWidgetItem(end))
			self.tableWidget.setItem(rowPosition , 2, QtGui.QTableWidgetItem(threshold))


def main():
	app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
	form = ScheduleApp()
	form.show()  # Show the form
	app.exec_()  # and execute the app


if __name__ == '__main__':
	main()  # run the main function
