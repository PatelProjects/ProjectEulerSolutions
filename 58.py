
currentNum = 1

multiplier = 1

primes = 0
alL = 0

def isPrime(number):
    
    if number == 2:
        return True
    if number == 3:
        return True
    
    if number %2 == 0:
        return False
    if number % 3 == 0: 
        return False
    
    i = 5
    w = 2
    
    while i *i <= number:
        if number % i == 0:
            return False
        
        i += w
        
        w = 6 - w
        
    return True

        
while True:
     
    for i in range(0,4):
        currentNum += 2*multiplier
        alL += 1
        if isPrime(currentNum):
            primes +=1
         
     
    if primes / alL < .1:
        print(2*multiplier-1)
        break
    multiplier += 1
     
    
    
# PRIME_PERCENT = 10
# n = 3; prime_count = 0 
# while True:
#     for i in (1, 2, 3):
#         prime_count += isPrime( n*n - i*(n-1))
#     ratio = (100 * prime_count) / (2*n - 1)
#     if ratio < PRIME_PERCENT: break
#     n += 2
# print(n) # 26241 765 ms
    
    