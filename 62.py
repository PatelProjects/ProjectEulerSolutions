import itertools

x = []
currentNumber = 0

print([''.join(i) for i in itertools.permutations("213")])

while True:
    currentCube = currentNumber ** 3
    count = 0
    
    for i in itertools.permutations(str(currentCube)):
        number = int(''.join(i))
        
        if (number ** 1/3).is_integer():
            count += 1  
            
    if count == 3:
        print(currentNumber)
        break  
    
    print(currentNumber)
         
    currentNumber += 1