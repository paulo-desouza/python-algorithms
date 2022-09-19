# Coin Change Problem!

# Given an N amount of money, return the minimum amount of coins possible to reach N.

# Solve this problem recursively.
def coin_change(n, coins):


    # default VALUE SET TO TARGET
    min_coins = n

    # base case check
    if n in coins:
        return 1

    else:
        # for every coin value that is less than or equal to my target value
        for i in [c for c in coins if c <= n]:
            
            # ADD A COIN COUNT + RECURSIVE
            num_coins = 1 + coin_change(n-i, coins)

            # RESET MINIMUM IF THE NEW NUM_COINS LESS THAN MIN_COINS
            if num_coins < min_coins:

                min_coins = num_coins
    

    return min_coins


    # Recursive solution is very slow

