coins = 'HHHHHTTTTT'
rounds = 0
while (True):
    rounds += 1
    print('select which coins to move by pressing space until the cursor is under the first coin you want to move')
    print(coins)
    coin = input()
    if ' ' in coins[len(coin):len(coin)+1]:
        rounds -= 1
        continue
    else:
        coin2 = coins[len(coin):len(coin)+2]
        if '  ' in coins:
            spot = coins.find('  ')
            if len(coin) > spot:
                coins = coins[0:spot] + coin2 + coins[spot+2:len(coin)] + '  ' + coins[len(coin)+2:]
            else:
                coins = coins[0:len(coin)] + '  ' + coins[len(coin)+2:spot] + coin2 + coins[spot+2:]
        else:
            print("Pick a side l/r")
            side = input()
            while side != 'l' and side != 'r':
                side = input()
            if side == 'l':
                coins = coin2 + coins[0:len(coin)] + '  ' + coins[len(coin)+2:]
            if side == 'r':
                coins = coins[0:len(coin)] + '  ' + coins[len(coin)+2:] + coin2

    if 'HTHTHTHTHT' in coins or 'THTHTHTHTH'in coins:
        print('WINNER')
        print(coins)
        break
    if coins[0:2] == '  ':
        coins = coins[2:]
    if coins[-2:] == '  ':
        coins = coins[:-2]
