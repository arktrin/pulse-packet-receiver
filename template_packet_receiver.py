# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template_packet_receive.ui'
#
# Created: Wed Feb 22 14:54:40 2017
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1042, 860)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.randCheck = QtGui.QCheckBox(Form)
        self.randCheck.setObjectName(_fromUtf8("randCheck"))
        self.gridLayout.addWidget(self.randCheck, 2, 2, 1, 1)
        self.plot = PlotWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy)
        self.plot.setObjectName(_fromUtf8("plot"))
        self.gridLayout.addWidget(self.plot, 0, 0, 1, 4)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.sizeSpin = QtGui.QSpinBox(Form)
        self.sizeSpin.setProperty("value", 10)
        self.sizeSpin.setObjectName(_fromUtf8("sizeSpin"))
        self.gridLayout.addWidget(self.sizeSpin, 2, 1, 1, 1)
        self.pixelModeCheck = QtGui.QCheckBox(Form)
        self.pixelModeCheck.setObjectName(_fromUtf8("pixelModeCheck"))
        self.gridLayout.addWidget(self.pixelModeCheck, 2, 3, 1, 1)
        self.startAverBtn = QtGui.QPushButton(Form)
        self.startAverBtn.setObjectName(_fromUtf8("startAverBtn"))
        self.gridLayout.addWidget(self.startAverBtn, 1, 0, 1, 1)
        self.stopAverBtn = QtGui.QPushButton(Form)
        self.stopAverBtn.setObjectName(_fromUtf8("stopAverBtn"))
        self.gridLayout.addWidget(self.stopAverBtn, 1, 1, 1, 1)
        self.resetAverBtn = QtGui.QPushButton(Form)
        self.resetAverBtn.setObjectName(_fromUtf8("resetAverBtn"))
        self.gridLayout.addWidget(self.resetAverBtn, 1, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.randCheck.setText(_translate("Form", "Randomize", None))
        self.label.setText(_translate("Form", "Size", None))
        self.pixelModeCheck.setText(_translate("Form", "pixel mode", None))
        self.startAverBtn.setText(_translate("Form", "Start average", None))
        self.stopAverBtn.setText(_translate("Form", "Stop average", None))
        self.resetAverBtn.setText(_translate("Form", "Reset avarage", None))

from pyqtgraph import PlotWidget
