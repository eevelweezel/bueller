#!/usr/bin/env python

# prime number under 1000000 that may be expressed as the longest sum of consecutive pri

def main():
    nums = [x for x in range(2,1000001)]
    s = 0
    for n in nums:
        c = 2
        print(str(c))
        print(str(n))
        while c < int(n/2)+1:
            if (n % c == 0) and (n != c) and n in nums:
                nums.remove(n)
            c += 1 
    for i in nums:
        if s + i < 1000000:        
            s += i
            print(str(s))
        else:
            break
    print(str(s)+' is the thing!')        
    return s

if __name__ == '__main__':
    main()   
    