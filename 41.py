# max is going to be either 4 or 7 because 1+2+3+4 and 1+2+...7 are not divisible by 3
# a number is divisible by 3 if and only if the digit sum (sum of digits) of the number is divisible by 3
  
def primeSieve(number):
       
    number += 1
    primes = dict()
       
    for i in range(2, number): 
        primes[i] = True
    
    for i in primes:
           
        factors = range(i,number, i)
           
        for f in factors[1:]:
            primes[f] = False
               
    return [i for i in primes if primes[i]==True]
      
def largestPandigitalPrime(number):
    numbers = ['1', '2', '3', '4', '5', '6' ,'7', '8', '9']
       
    for prime in primeSieve(number):
        setOfDigits = set(str(prime))
        lenPrime = len(str(prime))
     
        if lenPrime == len(setOfDigits) and setOfDigits == set(numbers[:lenPrime]):
            print(prime)
  
print(largestPandigitalPrime(7654321))



    
    
    



         

    