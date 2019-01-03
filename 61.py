import math
def triangle(n):
    return math.ceil(n*(n+1)/2)

def square(n):
    return n*n

def pentagonal(n):
    return math.ceil(n*(3*n-1)/2)

def hexagonal(n):
    return n*(2*n-1)

def heptagonal(n):
    return math.ceil(n*(5*n-3)/2)

def octagonal(n):
    return n*(3*n-2)





def results(n):
    return (3, triangle(n)), (4, square(n)), (5, pentagonal(n)), (6, heptagonal(n)), (7, heptagonal(n)), (8, octagonal(n))
 
              
def next(types, data):
    if len(types) == 6 and data[0] // 100 == data[-1] % 100:
        print(data, sum(data))
            
    else:
        for type, datA in ds.get( (types[-1], data[-1]), []):
            if type not in types:
                next(types + [type], data + [datA])
 
numbers = []
 
for i in range (0, 200):
    for type, data in results(i):
        if data >= 1000 and data <= 9999:
            numbers.append( (type, data) )
               
ds = {}

for type1, data1 in numbers:
    for type2, data2 in numbers:
        if type1 != type2 and data1 % 100 == data2 // 100:
            ds[type1, data1] = ds.get((type1, data1) , []) + [(type2, data2)]
 
               
for type, data in ds:
    next([type], [data])
     
    

 
 
 
# def fn(n):
#     return (3,n*(n+1)/2), (4,n*n), (5,n*(3*n-1)/2), (6,n*(2*n-1)), (7,n*(5*n-3)/2), (8,n*(3*n-2))
#    
# # def next(types, data):
# #     if len(types) == 6 and data[0] // 100 == data[-1] % 100:
# #         print(data, sum(data))
# #     else:
# #         for t, n in ds.get( (types[-1], data[-1]), []):
# #             if t not in types:
# #                 next(types+[t], data+[n])
#   
# p = []          # build a list of polygonal numbers with their type (type, pnum)
# n = 19          # first n for octogonal number > 999
#   
# while n < 141:  # last n for triangle numbers < 10000
#     for type, data in fn(n):
#         if 1000 <= data <= 9999 and data % 100 > 9:
#             p.append( (type, data) ) 
#     n+=1
#   
# ds = {}         # build a dictionary of tuples
# for t1, d1 in p:
#     for t2, d2 in p:
#         if t1 != t2 and d1 % 100 == d2 // 100:
#             ds[t1, d1] = ds.get((t1, d1),[]) + [(t2, d2)] 
#   
# print("Project Euler 61 Solution Set")
# for type, data in ds:
#     next([type], [data])

    
#Octagonal starts to become 4 digits long starting at term number 19. Ends at term number 58