#!/usr/bin/env python

import sys
import os

def main():
    d = 0
    e = 0
    g = 0
    with open('bigthing.txt','r') as f:
        n = f.readlines()
        for i in n:
            d += int(i)
            print(i)
        j = str(d)    
        k = j[0:10]
        print(k)
    return k

if __name__ == '__main__':
    main()