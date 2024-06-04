QUANTITY_OF_POSSIBLE_NUMBERS = 3
numbers_occurrences = [0] * QUANTITY_OF_POSSIBLE_NUMBERS
numbers = input().split("+")
quantity_of_numbers = len(numbers)
for i in range(quantity_of_numbers):
    numbers_occurrences[int(numbers[i]) - 1] += 1
sorted_numbers = []
for i in range(QUANTITY_OF_POSSIBLE_NUMBERS):
    occurrences_of_the_ith_number = numbers_occurrences[i]
    if occurrences_of_the_ith_number != 0:
        sorted_numbers += [i + 1] * occurrences_of_the_ith_number
rearranged_expression = ''
for i in range(quantity_of_numbers):
    current_number = sorted_numbers[i]
    rearranged_expression += f'{current_number}+' if i < quantity_of_numbers - 1 else str(current_number)
print(rearranged_expression)
