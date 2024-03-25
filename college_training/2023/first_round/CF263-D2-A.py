oneCoordinates = []
oneWasFound = False
for i in range(1, 6):
    row = input()
    if not oneWasFound:
        oneXCoordinate = row.find('1')
        if oneXCoordinate != -1:
            oneCoordinates = [oneXCoordinate // 2 + 1, i]
            oneWasFound = True
print(abs(3 - oneCoordinates[0]) + abs(3 - oneCoordinates[1]))
