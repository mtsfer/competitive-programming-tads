remix = input()
remix_length = len(remix)

original_song_words = []
original_song_word = ''

current_letter_index = 0

while current_letter_index < remix_length:
    possible_remix_word = remix[current_letter_index] == 'W' and current_letter_index + 2 < remix_length
    remix_word_found = False

    if possible_remix_word:
        word_under_analysis = remix[current_letter_index: current_letter_index + 3]
        remix_word_found = word_under_analysis == 'WUB'

    if remix_word_found:
        if original_song_word != '':
            original_song_words.append(original_song_word)
            original_song_word = ''
        current_letter_index += 2
    else:
        original_song_word += remix[current_letter_index]

    current_letter_index += 1

if original_song_word != '':
    original_song_words.append(original_song_word)
    original_song_word = ''

for i in range(len(original_song_words)):
    print(f' {original_song_words[i]}' if i != 0 else original_song_words[i], end='')
