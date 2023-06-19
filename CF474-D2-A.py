KEYS = "qwertyuiopasdfghjkl;zxcvbnm,./"

shifting_direction = input()
shifted_phrase = input()

shift_factor = 1 if shifting_direction == "L" else -1

corrected_phrase = "".join(KEYS[KEYS.index(shifted_letter) + shift_factor] for shifted_letter in shifted_phrase)

print(corrected_phrase)
