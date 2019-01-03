def addAndCheck(number):
    number += int(str(number)[::-1])
    
    if str(number) == str(number)[::-1]:
        return True
    
    return number
    
realCounter = 0 
for i in range(1, 10001):
    
    number = i 
    counter = 0
    while True:
        result = addAndCheck(number)
        if counter == 50:
            realCounter += 1
            break
            
        
        elif result != True:
            counter += 1
            number = result
           
        
        else:
            break
        

    
print(realCounter)