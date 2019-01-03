def primes(number):
       
    number += 1
    primes = dict()
       
    for i in range(2, number): 
        primes[i] = True
    
    for i in primes:
           
        factors = range(i,number, i)
           
        for f in factors[1:]:
            primes[f] = False
               
    return [i for i in primes if primes[i]==True]

def isPrime(number):
    if number == 2:
        return True
    
    if number == 3:
        return True
    
    if number % 2 == 0:
        return False
    
    if number % 3 == 0:
        return False
    
    i = 5
    w = 2
    
    while i * i <= number:
        if number % i == 0:
            return False
        
        i += w
        w = 6-w
        
    return True
    

minimum = 1
highest = 0
primes = primes(1000000)
for i in primes[:-minimum]:
    total = 0
    totalA = []
    count = 0
    for x in primes[primes.index(i)+1:]:
        total += x
        totalA.append(x)
        count += 1
        if total > 1000000:
            break
        if count > minimum:
            if isPrime(total):
                highest = total
                minimum = count
                
print(minimum)
print(highest)
       
    
s = "eifnweoi"


    
    
    
    
    
    
    