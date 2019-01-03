size = 3
stage = 2
total = 1

while True:
    
    starting = 4*stage*stage - 10*stage +7
    
    increment = (stage-1)*2
    total += starting 
    total += starting + increment
    total += starting + increment + increment
    total += starting + increment + increment + increment
    
    if size == 1001:
        break
    
    size += 2
    stage += 1
    
   
    
        
print(total)
        