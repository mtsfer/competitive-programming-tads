qtt_of_numbers, max_number = map(int, input().split())

qtt_of_good_numbers = 0
number_of_digits_to_found = max_number + 1

for _ in range(qtt_of_numbers):
    current_number = input()
    remaining_numbers_to_found = number_of_digits_to_found
    digit_presence = [0] * number_of_digits_to_found
    for digit in current_number:
        digit = int(digit)
        if digit > max_number:
            continue
        if digit_presence[digit] == 0:
            digit_presence[digit] = 1
            remaining_numbers_to_found -= 1
        if remaining_numbers_to_found == 0:
            qtt_of_good_numbers += 1
            break
print(qtt_of_good_numbers)
