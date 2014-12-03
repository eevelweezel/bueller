#!/usr/bin/env python


def main():
    n = 0
    c = 0
    while n < 200000000000:
        n += 1
        y = [1,n]
        c += n
        b = int(c/2)+1
        while b > 1:
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