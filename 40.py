
fractionPart =' '
currentNumber = 1

while len(fractionPart) <= 1000000:
    fractionPart += str(currentNumber)
    currentNumber += 1

print(int(fractionPart[1]) * int(fractionPart[10]) * int(fractionPart[100]) * int(fractionPart[1000]) * 
      int(fractionPart[10000]) * int(fractionPart[100000] * int(fractionPart[1000000])))    
    
    