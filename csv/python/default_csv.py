# -*- coding: utf-8 -*-
import time
import datetime
import csv

with open('default.csv', 'w') as f:
    size = 100000000
    writer = csv.writer(f, lineterminator='\n',quoting=csv.QUOTE_ALL) # 改行コード（\n）を指定しておく
    start = time.time()
    list = ["1","2","3","4","5", "6", "7", "8", "9", "10"]
    for i in range(0, size):
        writer.writerow(list)     # list（1次元配列）の場合

print("time={0}[s]".format(time.time() - start))
