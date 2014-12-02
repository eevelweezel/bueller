#!/usr/bin/env python

import sys


def main():
    a = str(2**1000)
    c = 0
    for b in a:
        c += int(b)
    print(str(c))
    return c

if __name__ == '__main__':
    main()
