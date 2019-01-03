largest =0
for x in range(100, 999):
    for y in range(100,999):
        suM = x*y
        if suM == int(str(suM)[::-1]) and suM > largest:
            largest = suM
            
            
print(largest)