file = open(r"C:\Users\Abhishek Patel\Desktop\words.txt", "r")
 
    
def triangleWordCount(file):
    
    triangleNumber = [0.5 * i * (i+1) for i in range(1, 46)]
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = 0
    
    words = []
    for line in file:
        words += line.split(",")

        
    for word in words:
        total = 0
        for letter in word.strip('"'):
            total += alphabet.index(letter) + 1
            
        if total in triangleNumber:
            count += 1
        
    return count

print(triangleWordCount(file))