#!/usr/bin/env python

from PyQt4 import QtGui, QtCore
import sys, os, time, datetime
import subprocess as sp
import template_schedule

now = datetime.datetime.now()
soon = now + datetime.timedelta(minutes=1)
then = now + datetime.timedelta(minutes=2)

def update_jobs():
	bash_command = 'update_jobs.py'
	process = sp.Popen(['bash','-c', bash_command], stdout=sp.PIPE)


class ScheduleApp(QtGui.QMainWindow, template_schedule.Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.setWindowTitle('Task scheduler')
		# self.tableWidget.setColumnWidth(2, 160)
		self.header = self.tableWidget.horizontalHeader()
		self.header.setResizeMode(QtGui.QHeaderView.Stretch)
		self.startDateTimeEdit.setDate(QtCore.QDate(soon.year, soon.month, soon.day))
		self.startDateTimeEdit.setTime(QtCore.QTime(soon.hour, soon.minute, soon.second))
		self.endDateTimeEdit.setDate(QtCore.QDate(then.year, then.month, then.day))
		self.endDateTimeEdit.setTime(QtCore.QTime(then.hour, then.minute, then.second))
		self.startDateTimeEdit.setMaximumDate(QtCore.QDate(2030, 12, 31))
		self.startDateTimeEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(now.year, now.month, now.day), QtCore.QTime(now.hour, now.minute, now.second)))
		self.endDateTimeEdit.setMaximumDate(QtCore.QDate(2030, 12, 31))
		self.endDateTimeEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(now.year, now.month, now.day), QtCore.QTime(now.hour, now.minute, now.second)))
		self.addTaskBtn.clicked.connect(self.add_task)
		self.rmSelTasksBtn.clicked.connect(self.rm_selected_tasks)
		self.updTableBtn.clicked.connect(self.update_table)
		self.checkbox_items = {}
		self.i_check = 0
		self.update_table()

	def add_task(self):
		start = self.startDateTimeEdit.dateTime().toPyDateTime().strftime("%d.%m.%y %H:%M")
		end = self.endDateTimeEdit.dateTime().toPyDateTime().strftime("%d.%m.%y %H:%M:%S")
		threshold = str(self.thresholdValSpin.value())
		text_for_at = self.startDateTimeEdit.dateTime().toPyDateTime().strftime("%H:%M %d.%m.%y")
		bash_command = 'echo "env DISPLAY=:0 pulse_packet_receiver.py" '+start+' '+end+' '+threshold+' | at '+text_for_at
		process = sp.Popen(['bash','-c', bash_command], stdout=sp.PIPE)
		self.update_table()

	def add_row(self, jobNumCol, startCol, endCol, thresholdCol, statusCol):
		rowPosition = self.tableWidget.rowCount()
		self.tableWidget.insertRow(rowPosition)

		self.checkbox_items[self.i_check] = QtGui.QTableWidgetItem()
		self.checkbox_items[self.i_check].setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
		self.checkbox_items[self.i_check].setCheckState(QtCore.Qt.Unchecked)
		self.tableWidget.setItem(rowPosition, 5, self.checkbox_items[self.i_check])
		self.i_check += 1

		self.tableWidget.setItem(rowPosition , 0, QtGui.QTableWidgetItem(jobNumCol))
		self.tableWidget.setItem(rowPosition , 1, QtGui.QTableWidgetItem(startCol))
		self.tableWidget.setItem(rowPosition , 2, QtGui.QTableWidgetItem(endCol))
		self.tableWidget.setItem(rowPosition , 3, QtGui.QTableWidgetItem(thresholdCol))
		self.tableWidget.setItem(rowPosition , 4, QtGui.QTableWidgetItem(statusCol))
		if statusCol == 'Done':
			self.tableWidget.item(rowPosition, 0).setBackground(QtGui.QColor(141, 244, 95))
			self.tableWidget.item(rowPosition, 1).setBackground(QtGui.QColor(141, 244, 95))
			self.tableWidget.item(rowPosition, 2).setBackground(QtGui.QColor(141, 244, 95))
			self.tableWidget.item(rowPosition, 3).setBackground(QtGui.QColor(141, 244, 95))
			self.tableWidget.item(rowPosition, 4).setBackground(QtGui.QColor(141, 244, 95))
			self.tableWidget.item(rowPosition, 5).setBackground(QtGui.QColor(141, 244, 95))

	def rm_selected_tasks(self):
		keys_to_delete = []
		for key, checkbox in self.checkbox_items.iteritems():
			if checkbox.checkState() == QtCore.Qt.Checked:
				row = checkbox.row()
				job_num = self.tableWidget.item(row, 0).text()
				start_end = self.tableWidget.item(row, 1).text()+' '+self.tableWidget.item(row, 2).text()
				status = self.tableWidget.item(row, 4).text()
				if status == 'Done':
					self.rm_task_from_jobs_txt(str(start_end))
				elif status == 'Pending':
					bash_command = 'atrm '+job_num
					process = sp.Popen(['bash','-c', bash_command], stdout=sp.PIPE)
				self.tableWidget.removeRow(row)
				keys_to_delete.append(key)
		for key in keys_to_delete:
			del self.checkbox_items[key]
		self.update_table()

	def rm_task_from_jobs_txt(self, start_end):
		with open('jobs.txt', 'r') as f:
			lines_to_leave = []
			lines = f.read().split('\n')[:-1]
			for i in xrange(len(lines)):
				if start_end not in lines[i]:
					lines_to_leave.append(i)
		with open('jobs.txt', 'w') as f:
			for i in xrange(len(lines)):
				if i in lines_to_leave:
					f.write(lines[i]+'\n')
					

	def jobs_to_table(self):
		with open('jobs.txt', 'r') as f:
			lines = f.read().split('\n')[:-1]
			for line in lines:
				row_vals = line.split(' ')
				self.add_row(row_vals[0], row_vals[1]+' '+row_vals[2], row_vals[3]+' '+row_vals[4], row_vals[5], row_vals[6])

	def update_table(self):
		self.tableWidget.setRowCount(0)
		self.checkbox_items = {}
		update_jobs()
		QtCore.QTimer.singleShot(400, lambda: self.jobs_to_table())


def main():
	app = QtGui.QApplication(sys.argv)
	form = ScheduleApp()
	form.show()
	app.exec_()


if __name__ == '__main__':
	main()  # run the main function
