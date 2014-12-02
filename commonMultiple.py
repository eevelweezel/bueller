#!/usr/bin/env python

import sys

def main(thing1=2, thing2=20):

    def factors(thing):
    # test for primes
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

    # factor stuff
        w = int(thing)
        z = w
        f = []
        m = 2
        g = 1 
    #   if z is prime, return to Go & collect $200
        if primacy_test(z) == 0:
            f.append(z)
    #   otherwise, factor stuff        
        else:
            while m < (z):
                for i in f:
                    g *= i
#                    print(str(g))            
                if w % m == 0:
                    print(str(m))
                    r = primacy_test(m)
                    w = w / m 
                    if r == 0:
                        f.append(m)
        #                print(str(m))
                    m = 2
                elif g == z: 
                    break       
                else:
                    m += 1
        #            print(str(m))
        print(str(f))
        return f
        
# back to the issue @ hand
    t = int(thing1)
    u = int(thing2)
    q = 1
    w = []
    for m in range(t,u):
        z = []
        z.append(factors(m))
        for i in z:
            for j in i:
                if j not in w:   # this needs to be smarter. e.g., (2 * 2 * 3) and (3 * 3) needs to be (2 * 2 * 3 * 3), not (2 * 3)
                    w.append(j)
    for x in w:
        print(str(x)+' '+str(q))
        q *= x
    print(str(q))
#    print(str('Factors of Thirteen '+str(factors(13))))
    return q
    
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
