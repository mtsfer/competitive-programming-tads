n = int(input())
previous_sequence = '1'
for i in range(2, n + 1):
    sequence = ''
    current_digit = previous_sequence[0]
    current_digit_qtt = 0
    previous_sequence_size = len(previous_sequence)
    for j in range(previous_sequence_size):
        element = previous_sequence[j]
        if element == current_digit:
            current_digit_qtt += 1
        else:
            sequence += f'{current_digit_qtt}{current_digit}'
            current_digit = element
            current_digit_qtt = 1
        if j == previous_sequence_size - 1:
            sequence += f'{current_digit_qtt}{current_digit}'
    previous_sequence = sequence
print(previous_sequence)
