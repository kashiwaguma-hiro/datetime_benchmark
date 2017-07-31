from datetime import datetime
import time

logtime_str = '20170101123456'
start = time.time()
for i in range(100000):
    dt = datetime(
        year=int(logtime_str[0:4]),
        month=int(logtime_str[4:6]),
        day=int(logtime_str[6:8]),
        hour=int(logtime_str[8:10]),
        minute=int(logtime_str[10:12]),
        second=int(logtime_str[12:14])
    )

print('{:.4f}sec'.format(time.time() - start))

