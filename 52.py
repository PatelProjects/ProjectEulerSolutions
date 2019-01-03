import time
startTime = time.time()
currentNum = 1


while True:
    if set(str(currentNum)) == set(str(currentNum *2)) == set(str(currentNum *3)) == set(str(currentNum *4)) == \
        set(str(currentNum *5)) == set(str(currentNum *6)):
        print(currentNum)
        break
    
    currentNum += 1
    
    
endTime = time.time()
print("completed in %s seconds" % (endTime - startTime, ))
    