aS = []
bS = []

for i in range(1,1000):
    for x in range(1,i):
        
        y = (x*x + i*i)**0.5
        
        if x + i + y == 1000:
            print(int(x*i*y))
            
        
            
        
