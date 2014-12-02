#!/usr/bin/env python

import sys
import math


def main():

    # fibonacci numbers < 1000
    def fibonacci():
        d = 0
        p = [1,1]
        q = 0
        for d in range(1010):
            d = p[-2]+p[-1]
            p.append(d)
        return p

    # k = a**2
    # n = (k+1)/2
    # b**2 = sum previous (n-1) terms
    # c**2 = sum previous n terms
    
    f = fibonacci()
    for x in f:
        a = 0 
        b = 0
        c = 0
        s = math.sqrt(x)
        if x > 1 and x % 2 != 0 and s % 1 == 0:   # x may be any odd Fibonacci sqr
            k = x
            a = s
            n = (k + 1)/2
            fib = f[0:int(n-1)]
            for i in fib: 
                c += i
            c = math.sqrt(c)
            fib.pop()
            for j in fib: 
                b += j
            b = math.sqrt(b)

        if a + b + c == 1000 and a**2 + b**2 == c**2:
           print('True')
           break
        else:
           print('Dammit')
    print('a: '+str(a)+' b: '+str(b)+' c: '+str(c))
    return 

if __name__ == '__main__':
    main()


