NUMBER = '1378'

last_digit_of_the_number = int(NUMBER[3])

power = int(input())

if power == 0:
    print(1)
else:
    remainder = power % 4

    last_digit_of_the_number_at_power = (last_digit_of_the_number ** remainder
                                         if remainder != 0
                                         else last_digit_of_the_number ** 4)

    print(str(last_digit_of_the_number_at_power)[-1])
