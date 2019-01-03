def isPermutation(number1, number2, number3):
    
    if set(number1) == set(number2) == set(number3):
        return True
    
    return False

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
        
    
def allPrime(number1, number2, number3):
    if isPrime(number1):
        if isPrime(number2):
            if isPrime(number3):
                return True
            
    return False
    


for i in range(1000, 3340):
    
    num1 = str(i)
    num2 = str(i+3330)
    num3 = str(i+3330*2)
    
    if isPermutation(num1, num2, num3):
        
        if allPrime(i, int(num2), int(num3)):
            print(num1+num2+num3)
    
    