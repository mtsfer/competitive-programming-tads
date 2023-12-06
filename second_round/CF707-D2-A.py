rows, columns = map(int, input().split())

is_colorful = False
for _ in range(rows):
    pixel_colors = input().split()
    for pixel_color in pixel_colors:
        if pixel_color != 'B' and pixel_color != 'W' and pixel_color != 'G':
            is_colorful = True
            break

print('#Color' if is_colorful else '#Black&White')
