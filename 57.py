from fractions import Fraction
import sys

count = 0
sys.setrecursionlimit(1012)

def rootTwo( iterations,count, answer = 3/2  ):
    
    if iterations == 1:
        
        return count
    
    else:
        answer = Fraction(str(1 + 1/(answer+1)))
       
               
        if len(str(answer.numerator)) > len(str(answer.denominator)):
            count += 1
            
       


        iterations -= 1
        return rootTwo(iterations,count, answer)
        
print(rootTwo(1000, count))


