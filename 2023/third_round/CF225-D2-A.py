number_of_dices = int(input())

top_most_number = int(input())
bottom_number_of_top_dice = 7 - top_most_number

input()  # side faces of the top most dice isn't relevant

for _ in range(number_of_dices - 1):
    visible_sides = list(map(int, input().split()))
    for side in visible_sides:
        if bottom_number_of_top_dice == side or bottom_number_of_top_dice == 7 - side:
            print("NO")
            exit(0)

print("YES")
