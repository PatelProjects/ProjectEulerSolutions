cache = {1: 1}
def collatz_count(n):
    if n not in cache:
        if n % 2 == 0:
            cache[n] = 1 + collatz_count(n / 2)
        else:
            cache[n] = 1 + collatz_count(3 * n + 1)
    return cache[n]

highest = 0 
number = 0
for i in range(1, 1000001):
    x =  collatz_count(i)
    if x > highest:
        highest = x
        number = i

print(number)
    












