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
        if n % i == 0:
            return False
        
        i += w
        w = 6 - w
        
    return True

x = [i for i in range(2,1000) if isPrime(i) == True]


total = 0
n = 4
y = 40

aF = 0
bF = 0
for a in range (-1000,1000):
    for b in x:
        n = 0
        while (isPrime(abs(n*n + n*a + b)) == True):
            n += 1
            
        if n > total:
            total = n
            aF = a
            bF = b
            

print(aF*bF)

        