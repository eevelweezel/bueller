#!/usr/bin/env python


import math
from numbers import Rational


def main():
    n = 1
    while n < 1000:
        d = 0
        a = n + 2
        b = (2/n) + 2
        print(str(b))
        c = math.sqrt(a**2 + b**2)
        n += 1
        if a + b + c == 1000:
            print('a: '+str(a)+' b: '+str(b)+' c: '+str(c))
            d = a * b * c
    print(str(d))
    return d
            
if __name__ == '__main__':
    main()

