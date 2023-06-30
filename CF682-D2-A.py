first_column_max, second_column_max = map(int, input().split())

bigger_column_max, smaller_column_max = ((first_column_max, second_column_max)
                                         if first_column_max > second_column_max
                                         else (second_column_max, first_column_max))

number_of_pairs = 0

for number in range(1, smaller_column_max + 1):
    number_of_pairs += (number + bigger_column_max) // 5 - number // 5

print(number_of_pairs)
