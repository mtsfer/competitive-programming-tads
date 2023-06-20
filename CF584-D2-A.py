number_of_digits, divisor = map(int, input().split())

inferior_limit = 10 ** (number_of_digits - 1)

upper_limit = 10 ** number_of_digits - 1

rest_of_division_between_inferior_limit_and_divisor = inferior_limit % divisor

number_with_digits_and_divisible = inferior_limit + (divisor - rest_of_division_between_inferior_limit_and_divisor
                                                     if rest_of_division_between_inferior_limit_and_divisor != 0 else 0)

print(number_with_digits_and_divisible if number_with_digits_and_divisible <= upper_limit else -1)
