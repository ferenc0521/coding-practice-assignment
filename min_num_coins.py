def min_num_coins(cents,coins):
    change=cents
    num_coins=0
    for coin in coins:
        num_coins += int(change/coin)
        change -= int(change/coin)*coin
        if change==0:
            return num_coins
def min_number_of_coins(cents,coins):
    min_coins = min([min_num_coins(cents,sorted(coins,reverse=True)),min_num_coins(cents,sorted(coins,reverse=True)[1:]),])
    return min_coins

print(31,[25,10,5,1],min_number_of_coins(31,[25,10,5,1]))
print(31,[25,10,1],min_number_of_coins(31,[25,10,1]))
print(31,[10,1],min_number_of_coins(31,[10,1]))
print(sorted([25,10,5,1],reverse=True))
print(list(filter(lambda x:x!=5,[25,10,5,1])))