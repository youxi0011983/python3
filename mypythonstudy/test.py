#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import math


class Solver(object):
    def demo(self, a, b, c):
        """

        @param a:
        @type a:float
        @param b:
        @type b: dict
        @param c:
        @type c: list
        """
        d = b ** 2 - 4 * a * c
        if d >= 0:
            disc = math.sqrt(d)
            root1 = (-b + disc) / (2 * a)
        else:
            raise

    def clen(self, a, b, c, d):
        """

        @param a:
        @type a: file
        @param b:
        @type b: str
        @param c:
        @type c: set
        @param d:
        @type d: frozenset
        """
        print(a,b,c)


Solver().demo()
Solver().clen()
