#!/usr/bin/env python

import sys

def main(thing):
    n = int(thing)
    d = 0
    p = [1,1]
    q = 0
    while d < n: 
        d = p[-2]+p[-1]
        p.append(d)
        if d % 2 == 0:
            q += d
        else:
            pass
    print(str(q))
    return q

if __name__ == '__main__':
    main(sys.argv[1])