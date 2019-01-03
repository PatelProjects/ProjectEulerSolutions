from math import factorial
count = 0

for i in range(3, 100000):
    suM = 0
    for x in str(i):
        suM +=  factorial(int(x))
        
    if suM == i:
      
        count +=  suM
        
print(count)
        
        