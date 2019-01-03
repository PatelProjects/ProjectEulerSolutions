
quoA = 0
x=0
total = 1
for num in range(10, 101):
    for den in range(num+1, 101):
        if (num != den) and ("0" not in str(num)) and ("0" not in str(den)):
            quo = num/den
            strNum = str(num)
            strDen = str(den)
            
            
            #!!!!!!!!!!!!!
            numA = strNum.translate({ord(c): None for c in strDen});
            denA = strDen.translate({ord(c): None for c in strNum});
            
            
            if numA != '' and denA != '':
                
                if int(denA) != 0 and quo == int(numA) / int(denA) and len(str(numA)) != len(str(num)):
              
                    print(quo)
                    total *= quo
                    x+=1
                    
print(1/total)