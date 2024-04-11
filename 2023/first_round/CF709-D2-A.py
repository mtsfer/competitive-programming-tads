number_of_oranges, max_orange_size, waste_limit = map(int, input().split())
times_waste_was_cleaned = 0
total_size_squeezed = 0
for orange_size in input().split():
    orange_size = int(orange_size)
    if orange_size > max_orange_size:
        continue
    total_size_squeezed += orange_size
    if total_size_squeezed > waste_limit:
        times_waste_was_cleaned += 1
        total_size_squeezed = 0
print(times_waste_was_cleaned)
