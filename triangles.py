#!/usr/bin/env python

def main():
    n = 0
    c = 0
    while n < 200000000000:
        y = []
        n += 1
        c += n
        b = c
        while b > 0:
            if c % b == 0:
                y.append(b)
            b -= 1
        print(str(n)+' '+str(len(y))+' '+str(c))
        if len(y) >= 500:
            print('Found it, its '+str(c))
            break
    return c

if __name__ == '__main__':
    main()