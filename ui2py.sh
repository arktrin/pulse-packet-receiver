#!/bin/bash

pyuic4 template_packet_receiver.ui -o template_packet_receiver.py
pyuic4 template_file_viewer.ui -o template_file_viewer.py
pyuic4 template_schedule.ui -o template_schedule.py

if [ -f "$PWD/template_packet_receiver.pyc" ]
then
	rm template_packet_receiver.pyc
	echo template_packet_receiver.pyc deleted	
fi


if [ -f "$PWD/template_file_viewer.pyc" ]
then
    rm template_file_viewer.pyc
    echo template_file_viewer.pyc deleted   
fi

if [ -f "$PWD/template_schedule.pyc" ]
then
    rm template_schedule.pyc
    echo template_schedule.pyc deleted   
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
file0="template_packet_receiver.py"
file1="template_file_viewer.py"

sed -i "s/$match0/$match0\n$insert0/" $file0
sed -i "s/$match1/$insert1/" $file0

sed -i "s/$match0/$match0\n$insert0/" $file1
sed -i "s/$match1/$insert1/" $file1
