for i in range(int(input())):
    word = input()
    word_length = len(word)
    print(f'{word[0]}{word_length - 2}{word[word_length - 1]}' if word_length > 10 else word)
