def divisorSum(n):
    total = 1
    
    index = 2
    
    while index * index < n:
        if n % index == 0:
            total += index + n//index
            
        index += 1
        
    if index * index == n:
        total += index
           
    return total


#4179871

abundant = []

for i in range(6, 28123-6):
    if divisorSum(i) > i:
        abundant.append(i)
        

print(len(abundant))
sumOfAbundant = [0]*28124

# x=4
# print(sumOfAbundant[28])
 
for i in range(0, len(abundant)):
    for k in range(i, len(abundant)):
        suM = abundant[i] + abundant[k]
        

        if suM <= 28123:
           
            if sumOfAbundant[suM] != 0: 
                x = 1
            else:
                sumOfAbundant[suM] = suM

total = 0
for x in range (1,len(sumOfAbundant)):
    if (sumOfAbundant[x] == 0):
        total +=x

print(total)




