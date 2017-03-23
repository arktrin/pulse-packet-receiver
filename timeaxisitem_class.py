# -*- coding: utf-8 -*-

import datetime
import pyqtgraph as pg

class TimeAxisItem(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super(TimeAxisItem, self).__init__(*args, **kwargs)

    def tickStrings(self, values, scale, spacing):
        return [datetime.datetime.utcfromtimestamp(float(value)/1e6).strftime("%H:%M:%S") for value in values]

