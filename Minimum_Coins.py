'''

Find the minimum number of coins needed to make up the amount

'''


def min_coins(cents,coins):
    if (cents ==0):
        return 0
    
    coins.sort(reverse = True)
    coins_used= []
    count = 0
    for coin in coins:
        while (coin <= cents):
            count+=1
            coins_used.append(coin)
            cents = cents-coin
            
    return (count)

coins =[25,10,5,1]
print(min_coins(43,coins))




