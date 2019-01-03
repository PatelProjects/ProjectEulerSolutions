def isPalindrome(string):
    if string == string[::-1]:
        return True
    
    
count = 0

for i in range(1, 1000000):
    
    
    
    if isPalindrome(str(i)) and isPalindrome("{0:b}".format(i)):
        count += i
    

print(count)

