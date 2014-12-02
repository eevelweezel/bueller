#!/usr/bin/env python

import sys
import os
import re

def main(thing):
    b = 0
    a = 0
    k = []
    with open(thing, 'r') as f:
        w = f.readline()
#        print(str(w))
        j = re.finditer('(?=(\d{13}))',w)  
        k = [(match.group(1)) for match in j]
#        print(str(k))
        for m in k:
            l = 1                    
            for n in m:
                l *= int(n)
                if l > a:
                    b = m
                    a = l                    
    print(str(a)+' '+str(b))
#    print(str(b))
    return b

if __name__ == '__main__':
    main(sys.argv[1])


