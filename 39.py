def integerRightTriangles(p):
    
    occurrences = [0 for i in range(0,p+1)]
    squaresOfNumbers = [i *i for i in range(0,p)]

    
    for number1 in range (1, p):
        
        for number2 in range(number1, p-1):

            number3Index = squaresOfNumbers[number1] + squaresOfNumbers[number2]
            
            if number3Index in squaresOfNumbers:
          
                total = number1 + number2 + squaresOfNumbers.index(number3Index)
                
                if total <= p:
                    
                    occurrences[total] += 1
            

    return occurrences.index(max(occurrences))
                
print("The answer is %d" % integerRightTriangles(100))