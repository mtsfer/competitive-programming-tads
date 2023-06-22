minimum_number, maximum_number = map(int, input().split())

insuficient_number_in_interval = maximum_number - minimum_number + 1 < 3

is_minimum_number_odd = minimum_number % 2 == 1

if insuficient_number_in_interval or (is_minimum_number_odd and maximum_number - minimum_number + 1 < 4):
    print('-1')
elif is_minimum_number_odd:
    print(minimum_number + 1, minimum_number + 2, minimum_number + 3)
else:
    print(minimum_number, minimum_number + 1, minimum_number + 2)
