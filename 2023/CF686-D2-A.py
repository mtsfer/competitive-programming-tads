amount_of_people_in_the_queue, amount_of_remaining_ice_cream_packs = map(int, input().split())
qtt_of_distress_kids = 0
while amount_of_people_in_the_queue > 0:
    amount_of_people_in_the_queue -= 1
    action, amount_of_ice_cream_packs = input().split()
    if action == '+':
        amount_of_remaining_ice_cream_packs += int(amount_of_ice_cream_packs)
    elif int(amount_of_ice_cream_packs) <= amount_of_remaining_ice_cream_packs:
        amount_of_remaining_ice_cream_packs -= int(amount_of_ice_cream_packs)
    else:
        qtt_of_distress_kids += 1
print(amount_of_remaining_ice_cream_packs, qtt_of_distress_kids)
