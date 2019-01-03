tree =  open("/Users/Abhishek Patel/Desktop/p067_triangle.txt", "r")
lines = [tree.readline() for i in range(0,100)]
print(lines[0])

rlines = lines[::-1]

print(rlines[0])