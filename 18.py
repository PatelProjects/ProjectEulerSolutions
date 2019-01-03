tree = open("/home/abhishek/Desktop/bob.txt", "r")
lines = [tree.readline() for i in range(15)]
rLines = []

for i in range(len(lines)-1 , 0, -1):
    rLines.append(lines[i])
    
bottom = rLines[0]

x = 1



bottomA = [0,1]
while len([int(i) for i in bottom.split()]) !=  2:
    
    top =  rLines[x]
    newRow = ""
    
    bottomA = [int(i) for i in bottom.split()]
    topA = [int(i) for i in top.split()]
    
    print(bottomA)
    print(topA)
    
    for i in range(0, len(topA)):
        newRow += ( str(topA[i] +  max(bottomA[i], bottomA[i+1])) + " ")
        
        

    bottom = newRow
    
    print(bottom)
    
    x += 1

print(max([int(i) for i in bottom.split()]))


