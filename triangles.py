#!/usr/bin/env python

import sys


def main(n):
    z = [x for x in range(1,int(n))]
    print(str(z))
    a = 0
    for i in z:
        y = []
        a += i
        b = a
        while b > 0:        
            if a % b == 0:
                y.append(b)
                b -= 1
        print(str(y))
#        if len(y) == 5:
#            print(str(i)+' has 20 factors')
    return y

if __name__ == '__main__':
    main(sys.argv[1])
