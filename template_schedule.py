# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template_schedule.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(794, 592)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 5, -1, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.thresholdValSpin = QtGui.QDoubleSpinBox(self.centralwidget)
        self.thresholdValSpin.setDecimals(1)
        self.thresholdValSpin.setMaximum(2500.0)
        self.thresholdValSpin.setSingleStep(0.1)
        self.thresholdValSpin.setProperty("value", 100.0)
        self.thresholdValSpin.setObjectName(_fromUtf8("thresholdValSpin"))
        self.gridLayout.addWidget(self.thresholdValSpin, 1, 3, 1, 1)
        self.startDateTimeEdit = QtGui.QDateTimeEdit(self.centralwidget)
        self.startDateTimeEdit.setDate(QtCore.QDate(2030, 1, 1))
        self.startDateTimeEdit.setTime(QtCore.QTime(0, 0, 25))
        self.startDateTimeEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(7930, 12, 31), QtCore.QTime(23, 59, 59)))
        self.startDateTimeEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2017, 1, 14), QtCore.QTime(0, 0, 0)))
        self.startDateTimeEdit.setMaximumDate(QtCore.QDate(7930, 12, 31))
        self.startDateTimeEdit.setMinimumDate(QtCore.QDate(2017, 1, 14))
        self.startDateTimeEdit.setObjectName(_fromUtf8("startDateTimeEdit"))
        self.gridLayout.addWidget(self.startDateTimeEdit, 1, 1, 1, 1)
        self.addTaskBtn = QtGui.QPushButton(self.centralwidget)
        self.addTaskBtn.setObjectName(_fromUtf8("addTaskBtn"))
        self.gridLayout.addWidget(self.addTaskBtn, 1, 4, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.endDateTimeEdit = QtGui.QDateTimeEdit(self.centralwidget)
        self.endDateTimeEdit.setTime(QtCore.QTime(0, 11, 17))
        self.endDateTimeEdit.setMaximumDate(QtCore.QDate(7930, 12, 31))
        self.endDateTimeEdit.setMinimumDate(QtCore.QDate(1817, 9, 14))
        self.endDateTimeEdit.setObjectName(_fromUtf8("endDateTimeEdit"))
        self.gridLayout.addWidget(self.endDateTimeEdit, 1, 2, 1, 1)
        self.rmTasksBtn = QtGui.QPushButton(self.centralwidget)
        self.rmTasksBtn.setObjectName(_fromUtf8("rmTasksBtn"))
        self.gridLayout.addWidget(self.rmTasksBtn, 2, 4, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Job number", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Start time", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "End time", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Threshold value, mV", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status", None))
        self.addTaskBtn.setText(_translate("MainWindow", "Add task", None))
        self.label_2.setText(_translate("MainWindow", "End time", None))
        self.label_3.setText(_translate("MainWindow", "Threshold value, mV", None))
        self.label.setText(_translate("MainWindow", "Start time", None))
        self.endDateTimeEdit.setDisplayFormat(_translate("MainWindow", "dd.MM.yy H:mm:ss", None))
        self.rmTasksBtn.setText(_translate("MainWindow", "Remove selected tasks", None))

