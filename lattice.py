#!/usr/bin/env python

import sys

def main(d):
    e = [x for x in range(1,(int(d)+1)*2)]
    print(str(d))
    line = []
    i = 1
    for f in e:
        l = [1]
        c = 1
        i = 1
        while i <= f:
            c = c * (f - i) / i
            l.append(c)
            i += 1
        line.append(l)
        print(str(l))
    return line

if __name__ == '__main__':
    main(sys.argv[1])
