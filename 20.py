def factorial(n):
    if n == 1:
        return 1
    
    else:
        return n* factorial(n-1)
    
x = str(factorial(100))

total = 0
for i in range(0,len(x)-1):
    total += int(x[i])
    
print(total)