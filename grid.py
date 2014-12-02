#!/usr/bin/env python

import sys
import os

def main():
    d = 0
    n = 0
    m = 0
    with open('grid.txt','r') as f:
        while m < 4:
            m += 1
            ws = f.readline()
            ws.replace('\n','')
            xs = f.readline()
            xs.replace('\n','')
            ys = f.readline()
            ys.replace('\n','')            
            zs = f.readline()
            zs.replace('\n','')            
            w = ws.split(' ')
            x = xs.split(' ')
            y = ys.split(' ')
            z = zs.split(' ')
            for i in w:
                print(str(w))
                n = 0
                while n < 16:
                    c = int(w[n])*int(w[n+1])*int(w[n+2])*int(w[n+3])
                    print(str(c))
                    n += 1        
                    if c > d:
                        d = c 
            for i in w:
                n = 0
                while n < 20:
                    c = int(w[n])*int(x[n])*int(y[n])*int(z[n])
#                    print(str(c))
                    n += 1        
                    if c > d:
                        d = c 
            for i in w:
                n = 0
                while n < 16:
                    c = int(w[n])*int(x[n+1])*int(y[n+2])*int(z[n+3])
                    n += 1        
                    if c > d:
                        d = c
            for i in w:
                n = 19
                while n > 2:
                    c = int(w[n])*int(x[n-1])*int(y[n-2])*int(z[n-3])
                    n -= 1        
                    if c > d:
                        d = c                    
        print('Answer is '+str(d))                 
    return d

if __name__ == '__main__':
    main()