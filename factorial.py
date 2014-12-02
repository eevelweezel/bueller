#!/usr/bin/env python


def main():
    z = [x for x in range(1,100)]
    m = 1
    n = 0
#    print(str(z))
    for x in z:
        m *= x
    c = str(m)
    for i in c:
       n += int(i)
    print(str(n))
    return n
if __name__ == '__main__':
    main()