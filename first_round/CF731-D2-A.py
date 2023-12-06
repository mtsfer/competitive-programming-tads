name = input()
pointer = ord('a')
number_of_rotations = 0
for next_letter in name:
    next_letter_decimal = ord(next_letter)
    distance_between = abs(pointer - next_letter_decimal)
    number_of_rotations += distance_between if distance_between <= 13 else 26 - distance_between
    pointer = next_letter_decimal
print(number_of_rotations)
