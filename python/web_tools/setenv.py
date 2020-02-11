#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os

dir="/home/eveline/python/web_tools/"


class MyEnv:
    def __init__(self):
        self.envFile = ''
        self.envs = {}

    def SetEnvFile(self, filename):
        self.envFile = filename

    def Save(self):
        outf = open(self.envFile, "w+")
        if not outf:
            print ("env file cannot be opened for write!")
        for k, v in self.envs.items():
            outf.write(k + "=" + v + "\n")
        outf.close()

    def Load(self):
        inf = open(self.envFile, "r+")
        if not inf:
            print ("env file cannot be opened for open!")
        for line in inf.readlines():
            k, v = line.split("=")
            self.envs[k] = v
        inf.close()

    def ClearAll(self):
        self.envs.clear()   

    def AddEnv(self, k, v):
        self.envs[k] = v

    def RemoveEnv(self, k):
        del self.envs[k]

    def PrintAll(self):
        for k, v in self.envs.items():
            print ( k + "=" + v )

  

if __name__ == "__main__" :
    myEnv = MyEnv()
    myEnv.SetEnvFile(dir+"myenv.txt")
    myEnv.Load()
    myEnv.AddEnv("MYDIR", dir+"mydir")
    myEnv.AddEnv("MYDIR2", dir+"mydir2")
    myEnv.AddEnv("MYDIR3", dir+"mydir3")
    myEnv.Save()
    myEnv.PrintAll()
    myEnv.RemoveEnv('MYDIR')
    myEnv.PrintAll()