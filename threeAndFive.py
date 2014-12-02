#!/usr/bin/env python

import sys

def main(thing):
    n = int(thing)
    o = 1
    p = 0
    while o < n: 
        if (o % 3 == 0) or (o % 5 == 0):
            p += o
            print(str(o))
        else:
            pass
            print(str(o))
        o += 1
    print(str(p))
    return p

if __name__ == '__main__':
    main(sys.argv[1])