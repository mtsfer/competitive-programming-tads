MATRIX_SIZE = 6
EMPTY_PLACE_SYMBOL = '-'
CURRENT_POSITION_SYMBOL = "#"


def print_matrix(matrix, current_x, current_y):
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            print(CURRENT_POSITION_SYMBOL if [i, j] == [current_x, current_y] else matrix[i][j],
                  end=' ' if j < MATRIX_SIZE - 1 else '')
        print()


def get_next_coordinate(current_x, current_y, letter_x, letter_y):
    # destination coordinate - current coordinate:
    # (> 0, > 0) => go to the next place in first diagonal
    # (> 0, < 0) => go to the previous place in first diagonal
    # (< 0, > 0) => go to the next place in second diagonal
    # (< 0, < 0) => go to the previous place in second diagonal
    x_difference = letter_x - current_x
    y_difference = letter_y - current_y

    if x_difference > 0:
        current_x += 1
    elif x_difference < 0:
        current_x -= 1
    if y_difference > 0:
        current_y += 1
    elif y_difference < 0:
        current_y -= 1

    return current_x, current_y


def main():
    matrix = [[EMPTY_PLACE_SYMBOL for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]

    current_x, current_y = map(int, input().split())

    word_size = int(input())
    letters_info = []
    for _ in range(word_size):
        letter, letter_x, letter_y = input().split()
        letter_x = int(letter_x)
        letter_y = int(letter_y)
        matrix[letter_x][letter_y] = letter
        letters_info.append([letter, letter_x, letter_y])

    print(f'Inicialmente nossa matriz e:')
    print_matrix(matrix, current_x, current_y)

    word_collected = ''
    next_letter_index_to_search = 0

    while next_letter_index_to_search < word_size:
        current_letter_info = letters_info[next_letter_index_to_search]
        letter_x = current_letter_info[1]
        letter_y = current_letter_info[2]

        current_x, current_y = get_next_coordinate(current_x, current_y, letter_x, letter_y)

        if [current_x, current_y] == [letter_x, letter_y]:
            word_collected += current_letter_info[0]
            matrix[current_x][current_y] = EMPTY_PLACE_SYMBOL
            next_letter_index_to_search += 1

        print(f'Por enquanto temos a palavra: {word_collected}')
        print_matrix(matrix, current_x, current_y)

    print(f'Acabamos nossa jornada e temos a palavra: {word_collected}')


if __name__ == '__main__':
    main()
