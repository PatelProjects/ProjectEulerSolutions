def isPandigital(number):

    
    if len(number) != 9:
        return False
    
    digits = set([1,2,3,4,5,6,7,8,9])
    
    digitsInNumber = set(int(i) for i in number)
    
    if digits == digitsInNumber:
        return True
    
    return False




def pandigitalMultiples():
    largest = 0
    
    for number in range(1,500000):
        
        multiple = 1
        tempNum = ""
        
        while len(tempNum) < 11:
            
            tempNum += str(number * multiple)
            
            if isPandigital(tempNum) and int(tempNum) > int(largest):
                largest = tempNum
                break
            
            multiple += 1
            
    return largest

print(pandigitalMultiples())
     