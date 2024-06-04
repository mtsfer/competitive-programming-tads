NUMBER_OF_PLAYERS = 2

number_of_levels = int(input())
levels = [0] * number_of_levels

levels_passed = 0

for _ in range(NUMBER_OF_PLAYERS):
    levels_current_player_can_pass = input()

    if levels_current_player_can_pass == '0':
        continue

    for level in levels_current_player_can_pass.split()[1:]:
        level = int(level)

        is_level_not_passed = levels[level - 1] == 0

        if is_level_not_passed:
            levels[level - 1] = 1
            levels_passed += 1

        if levels_passed == number_of_levels:
            break

print("I become the guy." if number_of_levels == levels_passed else "Oh, my keyboard!")
