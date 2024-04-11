shovel_price, coin_value = (int(i) for i in input().split())
shovels_to_buy = 1
while shovel_price * shovels_to_buy % 10 != 0 and (shovel_price * shovels_to_buy - coin_value) % 10 != 0:
    shovels_to_buy += 1
print(shovels_to_buy)
