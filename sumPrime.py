#!/usr/bin/env python

import sys


def main():
    z = [x for x in range(2,2000000)]
#    print(str(z))
    b = 2
    while b <= len(z):
        for i in z:
            if i % b == 0 and i != b:        
                z.remove(i)
                print(str(i))
        b += 1        
    c = 0       
    for i in z:
        c+= i
        print(str(c)+' '+str(i))
    return z

if __name__ == '__main__':
    main()