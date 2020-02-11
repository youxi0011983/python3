#!/usr/bin/python3
import string

pwd = string.digits+string.ascii_lowercase+string.ascii_uppercase
#pwd = string.digits+string.ascii_lowercase
lenpwd = len(pwd)
print(lenpwd)
bit=6

f  =  open('passdicttwo.txt','w')
print("Write to passdicttwo.txt...\n")
for i in range(lenpwd**bit):
    pp=''
    for j in range(bit):
        a=i%lenpwd
        pp=pwd[a]+pp
        #print (pp,pwd[a],"\n")
        i=i//36
    #print(pp)
    f.write(pp)
print("finish.....\n")
f.close()