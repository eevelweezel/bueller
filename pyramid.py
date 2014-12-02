#!/usr/bin/env python

import os

def main():
    with open('triangle18.txt','r+') as p:
        l = p.readlines()
        k = []
        c = 0 
        d = 0
        for i in l:
            m = i.split()
            if len(m) == 1:
                k.append(int(m[0]))
                d = 0
            else:
                a = int(m[d])
                b = int(m[d+1])
                if a > b:
                   k.append(a)
                else:
                   k.append(b)
                   d += 1  
            print(str(k))
#        print(str(k))
        c = 0
        for z in k:
            c += z
        print(str(c))     
    return c

if __name__ == '__main__':
    main()
