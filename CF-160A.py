COIN_MAXIMUM_VALUE = 100

input()
amount_of_money = 0
coins_grouped_by_value = [0] * COIN_MAXIMUM_VALUE

for coin_value in input().split():
    coin_value = int(coin_value)
    coins_grouped_by_value[coin_value - 1] += 1
    amount_of_money += coin_value

sorted_coins = []

for i in range(COIN_MAXIMUM_VALUE - 1, -1, -1):
    number_of_coins_of_current_value = coins_grouped_by_value[i]
    if number_of_coins_of_current_value != 0:
        sorted_coins += [i + 1] * number_of_coins_of_current_value

remaining_money = amount_of_money
twin_number_of_coins_collected = twin_collected_money = 0
current_coin_index = 0

while twin_collected_money <= remaining_money:
    current_coin_value = sorted_coins[current_coin_index]
    twin_number_of_coins_collected += 1
    twin_collected_money += current_coin_value
    remaining_money -= current_coin_value

    current_coin_index += 1

print(twin_number_of_coins_collected)
