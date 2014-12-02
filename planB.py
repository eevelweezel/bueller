#!/usr/bin/env python

import sys

def main(thing):

# return a list of the first n primes
    def count_primes(n):
        z = [2]
        c = 3
        while len(z) <= n:
            print(str(c))
            d = primacy_test(c)
            print(str(d))
            if d == 0:
                z.append(c)
            else:
                pass
            c += 1
        return z


# for primes > 1, return 0 if n is prime
    def primacy_test(n):
        b = n - 1
        p = 0
        while b > 2:
            if n % b != 0:
                b -= 1 
            else:
                p = 1
                break
        return p
        
    n = int(thing)
    if primacy_test(n) == 0:
        print(str(n)+' is prime.')
    else: 
        print(str(n)+' is not prime.')
    o = count_primes(n)
    print('The nth prime is '+str(o[n])) 
    return o
    
if __name__ == '__main__':
    main(sys.argv[1])
