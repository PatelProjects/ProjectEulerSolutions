def calculator(n):
    
    x = 1
    checked = []
    
    
    while True:
        if x in checked:
            break
        remainder = x % n
        checked.append(x)
        x = remainder * 10
        
    return len(checked)-1
   
highest = 0   
number = 0   
for i in range(1,1000):
    y = calculator(i)
    if y > highest:
        highest = y
        number = i
        

print(number)



