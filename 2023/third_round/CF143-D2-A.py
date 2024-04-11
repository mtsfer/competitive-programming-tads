NUMBER_OF_GEMS = 4
NUMBER_OF_ROWS = 2

MIN_GEM_VALUE = 1
MAX_GEM_VALUE = 9

rows_values = list(map(int, input().split()))
columns_values = list(map(int, input().split()))
diagonals_values = list(map(int, input().split()))


def brute_force_solution(gems_min_max_values):
    first_gem_min_max = gems_min_max_values[0]
    for first_gem_value in range(first_gem_min_max[0], first_gem_min_max[1] + 1):
        second_gem_min_max = gems_min_max_values[1]

        for second_gem_value in range(second_gem_min_max[0], second_gem_min_max[1] + 1):
            if first_gem_value == second_gem_value:
                continue
            third_gem_min_max = gems_min_max_values[2]

            for third_gem_value in range(third_gem_min_max[0], third_gem_min_max[1] + 1):
                if third_gem_value in [first_gem_value, second_gem_value]:
                    continue
                forth_gem_min_max = gems_min_max_values[3]

                for forth_gem_value in range(forth_gem_min_max[0], forth_gem_min_max[1] + 1):
                    if forth_gem_value in [first_gem_value, second_gem_value, third_gem_value]:
                        continue
                    first_row_match = rows_values[0] == first_gem_value + second_gem_value
                    second_row_match = rows_values[1] == third_gem_value + forth_gem_value
                    first_column_match = columns_values[0] == first_gem_value + third_gem_value
                    second_column_match = columns_values[1] == second_gem_value + forth_gem_value
                    first_diagonal_match = diagonals_values[0] == first_gem_value + forth_gem_value
                    second_diagonal_match = diagonals_values[1] == second_gem_value + third_gem_value
                    if (first_row_match
                            and second_row_match
                            and first_column_match
                            and second_column_match
                            and first_diagonal_match
                            and second_diagonal_match):
                        print(f"{first_gem_value} {second_gem_value}\n{third_gem_value} {forth_gem_value}")
                        return
    print(-1)


def get_min_and_max_values_for_gem_by_coord(coord):
    values = [rows_values[coord[0]], columns_values[coord[1]], diagonals_values[coord[2]]]

    min_gem_value = MIN_GEM_VALUE
    max_gem_value = MAX_GEM_VALUE

    for value in values:
        if value > MAX_GEM_VALUE:
            possible_min_value = value % MAX_GEM_VALUE
            if possible_min_value > min_gem_value:
                min_gem_value = possible_min_value
        else:
            possible_max_value = value - 1
            if possible_max_value < max_gem_value:
                max_gem_value = possible_max_value

    return min_gem_value, max_gem_value


def get_row_column_and_diagonal_from_index(index):
    row = index // NUMBER_OF_ROWS
    column = index % NUMBER_OF_ROWS
    diagonal = get_diagonal_by_coord(row, column)
    return row, column, diagonal


def get_diagonal_by_coord(row, column):
    return 0 if row == column else 1


def main():
    gems_min_max_values = []
    for i in range(NUMBER_OF_GEMS):
        coord = get_row_column_and_diagonal_from_index(i)
        gems_min_max_values.append(get_min_and_max_values_for_gem_by_coord(coord))

    brute_force_solution(gems_min_max_values)


main()
