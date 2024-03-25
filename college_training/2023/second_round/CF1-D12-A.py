theatre_height, theatre_width, flagstone_side = map(int, input().split())

number_of_flagstones_per_column = theatre_height // flagstone_side + (1 if theatre_height % flagstone_side != 0 else 0)
number_of_columns = theatre_width // flagstone_side + (1 if theatre_width % flagstone_side != 0 else 0)

print(number_of_flagstones_per_column * number_of_columns)
