#!/usr/bin/env python

import sys

def main(thing):

# because I can...
    def primacy_test(n):
        b = n - 1
        p = 0
        while b > 2:
            if n % b != 0:
                b -= 1 
            else:
                p = 1
                break
        return p

# actual problem
    w = int(thing)
    z = w
    f = []
    m = 2
#    print(str(m))
    while m < (z/2):
        g = 1 
        for i in f:
            g *= i
            print(str(g))
        if w % m == 0:
            r = primacy_test(m)
            w = w / m 
            if r == 0:
                f.append(m)
                print(str(m))
            m = 2
        elif g == z: 
            break       
        else:
            m += 1
            print(str(m))
    print(str(f))
    return f
if __name__ == '__main__':
    main(sys.argv[1])
