# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template_packet_receiver.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from timeaxisitem_class import TimeAxisItem

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(838, 757)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.thresholdWriteBtn = QtGui.QPushButton(Form)
        self.thresholdWriteBtn.setObjectName(_fromUtf8("thresholdWriteBtn"))
        self.gridLayout.addWidget(self.thresholdWriteBtn, 1, 1, 1, 1)
        self.plot = PlotWidget(Form, axisItems={'bottom': TimeAxisItem(orientation='bottom')})
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy)
        self.plot.setObjectName(_fromUtf8("plot"))
        self.gridLayout.addWidget(self.plot, 0, 0, 1, 5)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.windowLenSpin = QtGui.QSpinBox(Form)
        self.windowLenSpin.setMinimum(1)
        self.windowLenSpin.setMaximum(16)
        self.windowLenSpin.setProperty("value", 1)
        self.windowLenSpin.setObjectName(_fromUtf8("windowLenSpin"))
        self.gridLayout.addWidget(self.windowLenSpin, 4, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        self.saveDataBtn = QtGui.QPushButton(Form)
        self.saveDataBtn.setObjectName(_fromUtf8("saveDataBtn"))
        self.gridLayout.addWidget(self.saveDataBtn, 1, 4, 1, 1)
        self.thresholdValueSpin = QtGui.QDoubleSpinBox(Form)
        self.thresholdValueSpin.setDecimals(1)
        self.thresholdValueSpin.setMaximum(2500.0)
        self.thresholdValueSpin.setSingleStep(0.1)
        self.thresholdValueSpin.setObjectName(_fromUtf8("thresholdValueSpin"))
        self.gridLayout.addWidget(self.thresholdValueSpin, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.thresholdWriteBtn.setText(_translate("Form", "Write threshold value", None))
        self.label.setText(_translate("Form", "window length to average", None))
        self.saveDataBtn.setText(_translate("Form", "Save data", None))
        self.thresholdValueSpin.setSuffix(_translate("Form", " mV", None))

from pyqtgraph import PlotWidget
