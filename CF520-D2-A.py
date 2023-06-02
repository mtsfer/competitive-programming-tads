NUMBER_OF_ALPHABET_LETTERS = 26
DISTANCE_BETWEEN_UPPER_AND_LOWER = 32
FIRST_LOWERCASE_LETTER_DECIMAL = 97

sentence_length = int(input())
sentence = input()
alphabet_letters_boxes = [0] * NUMBER_OF_ALPHABET_LETTERS
filled_boxes = 0
current_letter_index = 0


def is_sentence_a_pangram() -> bool:
    return filled_boxes == NUMBER_OF_ALPHABET_LETTERS


def there_is_enough_remaining_letters_to_empty_boxes() -> bool:
    number_of_remaining_letters = sentence_length - current_letter_index
    number_of_empty_boxes = NUMBER_OF_ALPHABET_LETTERS - filled_boxes

    return number_of_remaining_letters >= number_of_empty_boxes


while there_is_enough_remaining_letters_to_empty_boxes() and not is_sentence_a_pangram():
    current_letter_in_decimal = ord(sentence[current_letter_index])
    current_letter_lowercase_in_decimal = (current_letter_in_decimal
                                           if current_letter_in_decimal >= FIRST_LOWERCASE_LETTER_DECIMAL
                                           else current_letter_in_decimal + DISTANCE_BETWEEN_UPPER_AND_LOWER)

    current_letter_box = current_letter_lowercase_in_decimal - FIRST_LOWERCASE_LETTER_DECIMAL
    if alphabet_letters_boxes[current_letter_box] == 0:
        alphabet_letters_boxes[current_letter_box] = 1
        filled_boxes += 1

    current_letter_index += 1

print("YES" if is_sentence_a_pangram() else "NO")
