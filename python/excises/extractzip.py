#!/usr/bin/python3
import zipfile


def extractFile(zipFile, password):
    try:
        zipFile.extractall(pwd=bytes(password, "utf8"))
        print("Unzip is successful...The password is"+password)
        return True
    except:
        pass


def main():
    zipFile = zipfile.ZipFile('./Python基础教程（第3版）（高清中文版PDF+高清英文版PDF+源代码）.rar')
    PwdLists = open('passdict.txt')
    for line in PwdLists.readlines():
        pwd = line.strip('\n')
        guess = extractFile(zipFile, pwd)
        if(guess is True):
            break


if __name__ == '__main__':
    main()