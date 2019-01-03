
def primes(number):
    number += 1
    prime = dict()
    
    for i in range(2, number):
        prime[i] = True
        
    for i in prime:
        
        factors = range(i, number, i)
        for f in factors[1:]:
            prime[f] = False
            
    return [i for i in prime if prime[i] == True]

def isPrime(number):
    if number == 2:
        return True
    
    if number == 3:
        return True
    
    if number %2 == 0:
        return False
    
    if number %3 == 0:
        return False
    
    
    i = 5
    w = 2
    
    while i *i <= number:
        if number % i == 0:
            return False
        
        i += w
        w = 6 -w
        
    return True
    

    

s = '0123456789'
#44587

 
for prime in primes(1000000):
    strPrime = str(prime)
    digits = []
    for digit in strPrime:
        if digit not in digits:
            digits.append(digit)
            if strPrime.count(digit) == 3:
                count = 0
                strCopy = strPrime
                index = 0
  
           
                while index <= 9:
                      
                    strCopy = strCopy.replace(digit, s[index])
                          
                    if len(strCopy.strip('0')) == len(strPrime) and isPrime(int(strCopy)):
                        count += 1
                     
                    
                    strCopy = strPrime
                    index += 1
                    if count == 8:
                        print("HIIIIIIIIIIII", strPrime)
                        break
                        
                    
                     
                

            
    
      
     