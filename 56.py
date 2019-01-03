max = 0

for a in range(1,100):
    for b in range(1,100):
        number = a ** b
        
        digitSum = 0
        for i in str(number):
            digitSum += int(i)
            
        if digitSum > max:
            max = digitSum
            
print(max)
            
            