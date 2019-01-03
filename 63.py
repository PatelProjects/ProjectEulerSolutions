
count = 0
for number in range(1,10):
    found = False
    for power in range(1, 1000):
        length = len(str(number ** power))
        if length == power:
            count += 1
            found = True
        elif found == True:
            break
        elif length > power:
            break
        if power == 999:
            print(number)
      
        
print(count)
    