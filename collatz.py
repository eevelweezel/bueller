#!/usr/bin/env python


def main():
    z = 1000000
    n = z
    c = 0
    d = 0
    while z >= 1:
        y = []
        while n > 1:
            if n % 2 == 0:
#                print(str(n))
                n = n/2
                y.append(n)
            else:
                n = 3*n + 1
#                print(str(n))
                y.append(n)
            if len(y) > c:
                c = len(y)
                d = z
        z -= 1 
        n = z        
    print(str(d)+' '+str(c))
    return d

if __name__ == '__main__':
    main()
