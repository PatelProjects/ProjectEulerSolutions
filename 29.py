numbers = []


for a in range(2, 101):
    for b in range(2,101):
        product = a**b
         
        if product not in numbers:
            numbers.append(product)

        
print(len(numbers))
    