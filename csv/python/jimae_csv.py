# -*- coding: utf-8 -*-
import time

with open('jimae.csv', 'w') as f:
    size = 100000000
    start = time.time()
    list = ["1","2","3","4","5", "6", "7", "8", "9", "10"]
    for i in range(0, size):
        str = '\"' + '\",\"'.join(list) + '\"'
        f.write(str + "\n")     # list（1次元配列）の場合

print("time={0}[s]".format(time.time() - start))
