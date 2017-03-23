#!/bin/bash

pyuic4 template_packet_receiver.ui -o template_packet_receiver.py

if [ -f "$PWD/template_packet_receiver.pyc" ]
then
	rm template_packet_receiver.pyc
	echo template_packet_receiver.pyc deleted	
fi

if [ -f "$PWD/timeaxisitem_class.pyc" ]
then
    rm timeaxisitem_class.pyc
    echo timeaxisitem_class.pyc deleted   
fi


match0="from PyQt4 import QtCore, QtGui"
insert0="from timeaxisitem_class import TimeAxisItem"
match1="self.plot = PlotWidget(Form)"
insert1="self.plot = PlotWidget(Form, axisItems={'bottom': TimeAxisItem(orientation='bottom')})"
file="template_packet_receiver.py"

sed -i "s/$match0/$match0\n$insert0/" $file
sed -i "s/$match1/$insert1/" $file
