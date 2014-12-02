#!/usr/bin/env python

import os

def main():
    with open('triangle18.txt','r+') as p:
        l = p.readlines()
#        print(str(l))
        k = []
        r = 0
        s = 0
        z = 0
        while s <= 13:
#            print(str(l[s+1]))
            o = l[s]
            q = l[s+1]
            m = o.split()
            n = q.split()
#            print(str(m))
#            print(str(n))
            s += 1
            if len(m) == 1:
                k.append(int(m[0]))
                r = 0
            else:
                a = int(m[r])
                b = int(m[r+1])
                c = int(n[r])
                d = int(n[r+1])
                e = int(n[r+2])
                if ((a + c) or (a + d)) > ((b + d) and (b + e)):
                   k.append(a)
                else:
                   k.append(b)
                   r += 1
            print(str(k))   
        if s == 14: 
#            print('check')
            o = l[-1]
            m = o.split()  
            a = int(m[r])
            b = int(m[r+1])
            if a > b:
                k.append(a)
            else:
                k.append(b)
        print(str(k))
        for y in k:
            z += y
        print(str(z))     
    return z

if __name__ == '__main__':
    main()
