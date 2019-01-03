def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
 
    realFactors = []
    i = 0
    while i < len(factors):
        count = 1
        if i < len(factors)-1:
            while i < len(factors)-1 and factors[i] == factors[i+1]:
                count += 1
                i += 1
       
        
        realFactors.append(factors[i]*count)
        i+= 1
            
    return realFactors

found = False
counter = 4

firstNum = prime_factors(0)
secondNum = prime_factors(1)
thirdNum = prime_factors(2)
fourthNum = prime_factors(3)
 
while found is False:
#     factors = set(prime_factors(counter) + prime_factors(counter+1)+ prime_factors(counter+2) + prime_factors(counter+3))
#  
    firstNum = secondNum
    secondNum = thirdNum
    thirdNum = fourthNum
    fourthNum = prime_factors(counter)
    
    allFactors = set(firstNum + secondNum + thirdNum + fourthNum)
    
    if len(allFactors) == 16:
        print(counter-3)
        found = True
    counter += 1
    
    
    