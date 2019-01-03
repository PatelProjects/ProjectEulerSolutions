count = 1

def isPrime(num):
    
    if num == 2:
        return True

    if num ==  3:
        return True
    
    if num % 2 == 0:
        return False
    
    if num % 3 == 0:
        return False
    
    i = 5
    w = 2
    
    while i * i <= num:
        if num % i == 0:
            return False

        i += w
        w = 6 - w

    return True
    
print(8)
print(len([i for i in range(1, 100) if isPrime(i)]))
    
# 
# for i in range(3, 1000001, 2):
#     y = str(i)
#     prime = True
#     for x in range(0, len(y)):
#         num = y[1:] + y[0]
#         
#         if not isPrime(int(num)):
#             prime = False
#         y = num
#     if prime == True:
#   
#         count += 1
#         
# print(count)
        
    
        
        
        
        
        
        