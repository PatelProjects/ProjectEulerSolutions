


target = 200
# total = 0
# 
# for a in range(target, -1, -200):
#     for b in range(a, -1, -100):
#         for c in range(b, -1, -50):
#             for d in range(c, -1, -20):
#                 for e in range(d, -1, -10):
#                     for f in range(e, -1, -5):
#                         for g in range(f, -1, -2):
#                             total += 1
#                               
# print(total)


coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [0]*(target+1)
ways[0] = 1


for coin in coins:
    for currentValue in range(coin, target+1):
        ways[currentValue] = ways[currentValue] + ways[currentValue-coin]

print(ways[target])

#73682


