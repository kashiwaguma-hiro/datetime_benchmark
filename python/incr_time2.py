# -*- coding: utf-8 -*-
import time
import datetime

size = 100000
date_from = datetime.datetime.strptime("20170101", '%Y%m%d')
date_to = datetime.datetime.strptime("20171231", '%Y%m%d')

ts = time.mktime(date_from.timetuple())
incr_sec = (time.mktime(date_to.timetuple()) - ts) / size

start = time.time()
for i in range(0, size):
    ts += incr_sec
    incr_time = datetime.datetime.fromtimestamp(ts)
    time_str = '{0}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{5:02d}'.format(incr_time.year, incr_time.month,incr_time.day,incr_time.hour,incr_time.minute,incr_time.second)
#    print(time_str)

print("time={0}[s]".format(time.time() - start))
