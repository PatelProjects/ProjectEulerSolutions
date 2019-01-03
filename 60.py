# from itertools import combinations, permutations
def prime_sieve(number):
    number += 1
     
    prime = dict()
     
    for i in range(2,number):
        prime[i] = True
         
    for i in prime:
        factors = range(i, number, i)
         
        for i in factors[1:]:
            prime[i] = False
         
    return [str(i) for i in prime if prime[i] == True and i != 2]



def is_prime(n):
    n = int(n)
    if n <= 1: return False
    if n <= 3: return True
    if n%2==0 or n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0 or n%(f+2) == 0: return False
        f+= 6
    return True





import itertools as iter 
primes = prime_sieve(10000)
set_size = 5

def make_chain(chain):
    if len(chain) == set_size:
        return chain 
    for p in primes:
        if p > chain[-1] and all_prime(chain+[p]):
            new_chain = make_chain(chain+[p])
            if new_chain:
                return new_chain
    return False  
        
def all_prime(chain):
    return all(is_prime(str(p[0]) + str(p[1])) for p in iter.permutations(chain, 2))

chain = 0
while not chain:
    chain = make_chain([primes.pop(0)])

print("Project Euler 60 Solution =", sum(map(int, chain)), chain)



