import itertools
from itertools import permutations

zToN = []

for i in range(0,10):
    zToN.append(i)
    
s = list(permutations(zToN))
print(s[999999])