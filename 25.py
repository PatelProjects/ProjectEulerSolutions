fibonacci = [1, 1]

i = 2
while True:
    number =  fibonacci[i-1] +  fibonacci[i-2]
    if len(str(number)) == 1000:
        print(i+1)
        break
    fibonacci.append(number)
    i+= 1