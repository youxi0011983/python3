#!/usr/bin/python3
import rarfile


def extractrarfile(rar_file, password):
    try:
        rar_file.extractall(pwd=bytes(password, "utf8"))
        print("Unzip is successful...The password is"+password)
        return True
    except:
        pass


def main():
    rar_file = rarfile.RarFile('D:/python3/python/excises/bookpython.rar')
    PwdLists = open('passdict.txt')
    for line in PwdLists.readlines():
        pwd = line.strip('\n')
        guess = extractrarfile(rar_file, pwd)
        if(guess is True):
            break


if __name__ == '__main__':
    main()
