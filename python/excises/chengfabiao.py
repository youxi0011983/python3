#!/usr/bin/env python3

for i in range(9,0,-1):
    for j in range (1,i):
        print("\t",end="")
    for k in range (i,10):
        print("%dx%d=%d" % (i,k,k*i), end="\t")
    print()