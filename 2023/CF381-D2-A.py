left_most_available_card_index = 0
right_most_available_card_index = int(input()) - 1
cards = input().split()
sereja_points = dima_points = 0
for i in range(len(cards)):
    left_most_card = int(cards[left_most_available_card_index])
    right_most_card = int(cards[right_most_available_card_index])
    if left_most_card > right_most_card:
        higher_card = left_most_card
        left_most_available_card_index += 1
    else:
        higher_card = right_most_card
        right_most_available_card_index -= 1
    if i % 2 == 0:
        sereja_points += higher_card
    else:
        dima_points += higher_card
print(sereja_points, dima_points)
