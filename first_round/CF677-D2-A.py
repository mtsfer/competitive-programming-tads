(numberOfFriends, fenceHeight) = (int(x) for x in input().split())
minimumRoadWidth = 0
for y in input().split():
    minimumRoadWidth += 1 if int(y) <= fenceHeight else 2
print(minimumRoadWidth)
