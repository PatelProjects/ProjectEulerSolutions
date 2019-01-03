def year(n):
    
    if n % 100 == 0:
        
        if n % 400 == 0:
            return 2
        else:
            return 1
    
    if n % 4 == 0:
        return 2
    
    return 1

    
total  = 0 

temp = 0 
for i in range(1900, 2001):
    
    temp += year(i)
    
    if temp == 7:
        temp = 0
        total += 1
        
    if temp == 8:
        temp = 1
    
    
print(total)    

# incomplete
    
    
    
    