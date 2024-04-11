ORIENTATIONS = ['N', 'L', 'S', 'O']
NUMBER_OF_ORIENTATIONS = 4

x_limit_index, y_limit_index = map(int, input().split())

death_coordinates = []
number_of_robots_in_training = int(input())
for _ in range(number_of_robots_in_training):
    current_x, current_y, orientation = input().split()
    current_x = int(current_x)
    current_y = int(current_y)
    orientation_index = ORIENTATIONS.index(orientation)

    is_lost = False
    commands_sequence = input()
    for command in commands_sequence:
        # print(f"Go to {command}:")
        if command == 'D':
            orientation_index = (orientation_index + 1) % NUMBER_OF_ORIENTATIONS
            orientation = ORIENTATIONS[orientation_index]
        elif command == 'E':
            orientation_index = orientation_index - 1 % NUMBER_OF_ORIENTATIONS
            orientation = ORIENTATIONS[orientation_index]
        elif command == 'F':
            if [current_x, current_y, orientation_index] in death_coordinates:
                # print('Skipping death coordinate')
                continue
            if orientation == 'N':
                if current_y + 1 > y_limit_index:
                    is_lost = True
                    break
                current_y += 1
            elif orientation == 'L':
                if current_x + 1 > x_limit_index:
                    is_lost = True
                    break
                current_x += 1
            elif orientation == 'S':
                if current_y - 1 < 0:
                    is_lost = True
                    break
                current_y -= 1
            elif orientation == 'O':
                if current_x - 1 < 0:
                    is_lost = True
                    break
                current_x -= 1
        # print(current_x, current_y, orientation)
    final_coord_and_orientation = f'{current_x} {current_y} {orientation}'
    if is_lost:
        print(f'{final_coord_and_orientation} PERDIDO')
        death_coordinates.append([current_x, current_y, orientation_index])
    else:
        print(final_coord_and_orientation)
    # print("---------------------")
# print(death_coordinates)
