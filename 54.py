
poker = open("/home/abhishek/Desktop/poker.txt")


for line in poker:
    cards = poker.readline().strip('\n').split(' ')
    playerOneCards = []
    playerTwoCards =[]
    for card in range(0,5):
        playerOneCards.append(cards[card])
    
    for card in range(5,10):
        playerTwoCards.append(cards[card])
        
    
        
    print(playerOneCards)
    print(playerTwoCards)
    

print(['q','q','q','q','q'].remove('q'))

def playerOneWin(playerOneCards, playerTwoCards):
    
    values = '23456789TJQKA'
    
    playerOneValues = [i[0] for i in playerOneCards]
    playerOneSuit = [i[1] for i in playerOneCards]
     
    playerTwoValues = [i[0] for i in playerTwoCards]
    playerTwoSuit = [i[1] for i in playerTwoCards]
    
    
        
        
        
        

            
                
        
         
         
# print(playerOneWin(['1S','1S','1S','1S','1S'], ['1S','1S','1S','1S','1S']))




def count(Array):

    dic = dict()
    
    for i in Array:
        if i not in dic:
            dic[i] = 1
            
        else:
            dic[i] += 1
    x =  [i for i in dic.values()]
    x.sort(reverse=True)
    return x
    
    
print(count(['a','a','a','a','b']))
    
    
    
