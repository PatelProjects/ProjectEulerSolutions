


from math import factorial

def combinations(n, r):
    return ( (factorial(n)) / (factorial(r)* factorial(n-r)) )

count = 0
for n in range(1, 101):
    for r in range(1, n):
        if combinations(n,r) > 1000000:
            count += 1
print(count)