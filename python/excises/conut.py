#!/usr/bin/env python3
import os
import sys

n = 100
 
count = 0
counter = 1
while counter <= n:
    count= count+ counter
    counter += 1
 
print("1 到 %d 之和为: %d" % (n,count))

print(sum(range(101)))