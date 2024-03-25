reference_number, target_position = map(int, input().split())

nth_odd_number = 1 + 2 * (target_position - 1)

if nth_odd_number <= reference_number:
    print(nth_odd_number)
else:
    number_of_odd_numbers_before_reference = (reference_number // 2
                                              if reference_number % 2 == 0
                                              else (reference_number // 2) + 1)

    even_number_position = target_position - number_of_odd_numbers_before_reference
    even_number = 2 * even_number_position

    print(even_number)
