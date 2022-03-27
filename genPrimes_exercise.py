# MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
"""
Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...


"""

def genPrimes():
    '''
    p, primes = 1, []
    while True:
        p += 1
        for i in primes:
            if p % i == 0:
                break
        else:
            primes.append(p)
            yield p
    '''
    p = []
    x = 1
    while True:
        x += 1 
        m = 0
        for i in p:
            if (x%i) == 0:
                m += 1
            else:
                pass
        if m == 0:
            p.append(x)
            yield x
        elif m!=0:
            m = 0
            #print("Not a prime")
f = genPrimes()
#f.__next__()