# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template_file_viewer.ui'
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
        Form.resize(944, 757)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 1, 1, 1)
        self.windowLenSpin = QtGui.QSpinBox(Form)
        self.windowLenSpin.setMinimum(1)
        self.windowLenSpin.setMaximum(16)
        self.windowLenSpin.setProperty("value", 1)
        self.windowLenSpin.setObjectName(_fromUtf8("windowLenSpin"))
        self.gridLayout.addWidget(self.windowLenSpin, 4, 2, 1, 1)
        self.plot = PlotWidget(Form, axisItems={'bottom': TimeAxisItem(orientation='bottom')})
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy)
        self.plot.setObjectName(_fromUtf8("plot"))
        self.gridLayout.addWidget(self.plot, 0, 0, 1, 6)
        self.winTypeComboBox = QtGui.QComboBox(Form)
        self.winTypeComboBox.setObjectName(_fromUtf8("winTypeComboBox"))
        self.winTypeComboBox.addItem(_fromUtf8(""))
        self.winTypeComboBox.addItem(_fromUtf8(""))
        self.winTypeComboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.winTypeComboBox, 2, 2, 1, 1)
        self.loadDataBtn = QtGui.QPushButton(Form)
        self.loadDataBtn.setObjectName(_fromUtf8("loadDataBtn"))
        self.gridLayout.addWidget(self.loadDataBtn, 2, 4, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 3, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.exportImgBtn = QtGui.QPushButton(Form)
        self.exportImgBtn.setObjectName(_fromUtf8("exportImgBtn"))
        self.gridLayout.addWidget(self.exportImgBtn, 4, 4, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "window length to average", None))
        self.winTypeComboBox.setItemText(0, _translate("Form", "rectangular", None))
        self.winTypeComboBox.setItemText(1, _translate("Form", "tukey", None))
        self.winTypeComboBox.setItemText(2, _translate("Form", "hann", None))
        self.loadDataBtn.setText(_translate("Form", "Load data", None))
        self.label_2.setText(_translate("Form", "window type", None))
        self.exportImgBtn.setText(_translate("Form", "Export image", None))

from pyqtgraph import PlotWidget
