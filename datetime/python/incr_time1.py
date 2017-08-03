# -*- coding: utf-8 -*-
import time
import datetime

def calculate_diff_seconds(date_from, date_to):
  date_to =  date_to + datetime.timedelta(seconds=-1)# TOを指定日以内に丸めて扱う
  delta = date_to - date_from
  return (delta.days * 24 * 60 * 60) + delta.seconds

size = 100000000
date_from = datetime.datetime.strptime("20170101", '%Y%m%d')
date_to = datetime.datetime.strptime("20171231", '%Y%m%d')

diff_second = float(calculate_diff_seconds(date_from, date_to))
incr_sec = diff_second / size
incr_time = date_from

start = time.time()
for i in range(0, size):
     incr_time = incr_time + datetime.timedelta(seconds= +incr_sec)
     time_str =  incr_time.strftime('%Y-%m-%d %H:%M:%S')

print("time={0}[s]".format(time.time() - start))




