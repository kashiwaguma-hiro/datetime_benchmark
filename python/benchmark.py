# -*- coding: utf-8 -*-
import sys
import time
from datetime import datetime
from datetime import timedelta

date_from = datetime.strptime("2017-09-01", '%Y-%m-%d')
ts = time.mktime(date_from.timetuple())
start = time.time()
for i in range(100000):

    data_datetime = datetime.fromtimestamp(ts)
    datetime_str = '{0}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{5:02d}'.format(data_datetime.year, data_datetime.month, data_datetime.day, data_datetime.hour, data_datetime.minute, data_datetime.second)

print('{:.4f}sec'.format(time.time() - start))
