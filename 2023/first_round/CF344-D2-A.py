numberOfMagnets = int(input())
currentPivot = input()
numberOfGroups = 1
for i in range(0, numberOfMagnets - 1):
    magnet = input()
    if magnet == currentPivot:
        continue
    numberOfGroups += 1
    currentPivot = magnet
print(numberOfGroups)
