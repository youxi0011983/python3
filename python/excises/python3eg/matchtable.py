#!/usr/bin/python3

if __name__ == '__main__':
    print('\n'.join(' '.join("%dx%d=%-2d" % (x, y, x*y) for x in range(1, y+1)) for y in range(1, 10)))