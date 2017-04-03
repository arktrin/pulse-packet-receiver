#!/usr/bin/env python

from PyQt4 import QtGui  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication

import template_schedule  # This file holds our MainWindow and all design related things

# it also keeps events etc that we defined in Qt Designer
import os  # For listing directory methods


class ExampleApp(QtGui.QMainWindow, template_schedule.Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)  
		self.btnBrowse.clicked.connect(self.browse_folder)

	def browse_folder(self):
		self.listWidget.clear() # In case there are any existing elements in the list
		directory = QtGui.QFileDialog.getExistingDirectory(self, "Pick a folder")

		if directory: # if user didn't pick a directory don't continue
			for file_name in os.listdir(directory): # for all files, if any, in the directory
				self.listWidget.addItem(file_name)  # add file to the listWidget


def main():
	app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
	form = ExampleApp()  # We set the form to be our ExampleApp (design)
	form.show()  # Show the form
	app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
	main()  # run the main function
