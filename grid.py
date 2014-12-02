#!/usr/bin/env python

import sys
import os


def main():
    d = 0
    n = 0
    with open('grid.txt','r') as f:
        w = f.readlines()
#        for x in w:
#            n = 0
#            c = 0
#            for y in x:        
#                c += int(y) 
#                if c > d:
#                    d = c
 #               n += 1 
        for x in w:
            n = 0
            o = 0
            y = str(x)
            for i in y:
                m = y[n:n+4]    
                for j in m: 
                    o += j
                if o > d:
                    d = o 
        for x in w:
            n = 3
            while n < 19:
                c = int(w[w.index(x)][n])+int(w[w.index(x)-1][n-1])+int(w[w.index(x)-2][n-2])+int(w[w.index(x)-3][n-3])
                n += 1        
                if c > d:
                    d = c
        for x in w:
            n = 0
            while n < 19:
                c = int(w[w.index(x)][n])+int(w[w.index(x)+1][n])+int(w[w.index(x)+2][n])+int(w[w.index(x)+3][n])
                n += 1        
                if c > d:
                    d = c                    
    return d

if __name__ == '__main__':
    main()
