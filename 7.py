
x = 2
current = 4
latest = 0

def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

while x != 10001:
    
    if isprime(current):
        x += 1
        latest = current
    current += 1
    
    

print(latest)
    