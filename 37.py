#Good

def primes_sieve1(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): 
        primes[i] = True
 
    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]
 




def truncate_left_right(num):
    s = str(num)
    retVal = set()
    for i in range(1, len(s)):
        retVal.add(int(s[i:]))
        retVal.add(int(s[:i]))
    return retVal

def solve(upper):
    primes = set(primes_sieve1(1000000))
    trunc_primes = set()
    for prime in primes:
        if truncate_left_right(prime) <= primes:
            trunc_primes.add(prime)
    return [p for p in trunc_primes if p > 7]

print(sum(solve(1000000)))

#748317



