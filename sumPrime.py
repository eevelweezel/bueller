#!/usr/bin/env python

import math
import sys


def main():
    z = [x for x in range(2,2000001)]
    n = 1
    for i in z:
        b = 2*n
        if i % b == 0:        
            z.pop(z.index(i))
            print(str(i))
        
    c = 5       
    for i in z:
        c+= i
        print(str(c)+' '+str(i))
    return z

if __name__ == '__main__':
    main()
