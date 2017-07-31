from datetime import datetime
import time

logtime_str = '20170101123456'
start = time.time()
for i in range(100000):
    dt = datetime.strptime(logtime_str, '%Y%m%d%H%M%S')

print('{:.4f}sec'.format(time.time() - start))
