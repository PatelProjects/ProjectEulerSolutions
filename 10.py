
def isPrime(n):
    
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    
    i = 5
    w = 2
    
    while i *i <= n:
        if n%i == 0:
            return False
        
        i += w
        w = 6 - w
    
    return True

x = 3
total = 2

while x <= 2000000:
    
    if isPrime(x) == True:
        total += x

    
    x+= 2
    
print(total)
    
    
    
#     
# marked = [0] * 2000000
# 
# currentValue = 3
# 
# numberOfPrimes = 2
# 
# while currentValue < 2000000:
#     
#     if marked[currentValue] == 0:
#         numberOfPrimes += currentValue
#         i = currentValue
#         
#         while i < 2000000:
#             marked[i] = 1
#             i += currentValue
#             
#     currentValue += 2
#     
# print(numberOfPrimes)


