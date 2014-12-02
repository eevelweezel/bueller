#!/usr/bin/env python

import sys

def main():

    def rev(s): 
        return s[::-1]
    y = []    
    z = []
    for n in range(10000,998001):
        if rev(str(n)) == str(n):
            z.append(n)
    for i in z:
        for n in range(99,1000):
            s = i / n
            if i / n > 99 and i % n == 0 and i / n < 1000:
                print(str(s)+' = '+str(i)+' / '+str(n))
                y.append(i)
    y.sort()
    print(str(y[-1]))
    return y       
    
if __name__ == '__main__':
    main()