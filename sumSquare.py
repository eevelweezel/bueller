#!/usr/bin/env python

import sys

def main(thing):
    m = int(thing)+1
    j = 0
    k = 0
    for n in range(1,m):
        j += n*n
        k += n
    print(str(j))    
    print(str(k**2))
    l = (k**2) - j
    print(str(l))
    return l    
    
if __name__ == '__main__':
    main(sys.argv[1])