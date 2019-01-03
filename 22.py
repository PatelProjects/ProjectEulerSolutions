names = open("/home/abhishek/Desktop/names.txt" , "r")
x = names.readline()
y = [i.strip('"') for i in x.split(",")]

y.sort()

import string

letters=[i for i in string.ascii_uppercase]

order = 1

final = 0
for i in y:
    total = 0

    for letter in i:
        total += (letters.index(letter)+1)
    final += total * order
    order += 1

print(final)


