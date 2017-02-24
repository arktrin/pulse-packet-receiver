#!/bin/bash

pyuic4 template_packet_receiver.ui -o template_packet_receiver.py
if [ -f "$PWD/template_packet_receiver.pyc" ]
then
	rm template_packet_receiver.pyc
	echo template_packet_receiver.pyc deleted	
fi
