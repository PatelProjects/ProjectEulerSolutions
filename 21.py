def divisorSum(n):
    sum = 1
    
    if n % 2 == 0:
        x = n // 2
        sum += 2 + x
    
    i = 3
    
    while i * i <=  n:
        if n % i == 0:
            
            x = n // i
            sum += i + x
           
        
        i += 1
        
    return sum

alreadyChecked = []

total = 0

for i in range(2, 10000):
    alreadyChecked.append(i)
    x = divisorSum(i)
    y = divisorSum(x)
    if i == y and x not in alreadyChecked:
        total += (i + x)
        
print(total)


    
    