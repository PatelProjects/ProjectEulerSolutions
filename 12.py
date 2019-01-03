def divisors(n):
    total = 1
    while n%2 == 0:
        n /= 2
        total += 1
    
    i = 3
    
    while i*i <= n:
        prime = 1 
        while n % i == 0:
            prime += 1
            n /= i
        
        total *= prime
        i += 2
    
    if n != 1:
        total *= 2
    
    return total



n = 1
    
while True:
    number = int(n*(n+1)/2)
           
    if divisors(number) > 500:
        print(number)
        break
          
    n+= 1
    

# import time   
# s = time.time()
# for i in range(1,100):
#     divisors(i)
# print(time.time()-s)
    

    
#76576500.0

    
