
total =0

i = 10
while i <  len(str(i))* 9**5:
    strNum = str(i)
    tTotal = 0
    for k in strNum:
        tTotal += (int(k))**5
    if i == tTotal:
        total += i
        
    i+=1
        
print(total)


#443839