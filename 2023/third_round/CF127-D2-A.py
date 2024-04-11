from math import sqrt

WRITING_SPEED = 50


def calculate_distance_between_two_points(coordinates1: list, coordinates2: list):
    return sqrt(abs(coordinates1[0] - coordinates2[0]) ** 2 + abs(coordinates1[1] - coordinates2[1]) ** 2)


number_of_lines, number_of_papers = map(int, input().split())

accumulated_distance = 0
previous_coordinate = list(map(int, input().split()))

for i in range(number_of_lines - 1):
    current_coordinate = list(map(int, input().split()))
    accumulated_distance += calculate_distance_between_two_points(previous_coordinate, current_coordinate)
    previous_coordinate = current_coordinate

print(accumulated_distance * number_of_papers / WRITING_SPEED)
