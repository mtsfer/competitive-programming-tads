number_of_groups = int(input())

for k in range(number_of_groups):
    number_of_members = int(input())

    members_names = input().split()
    members_balance = [0] * number_of_members

    for i in range(number_of_members):
        gift_info = input().split()
        current_member_name = gift_info[0]
        current_member_index = members_names.index(current_member_name)
        current_member_balance = members_balance[current_member_index]

        money_to_gifts = int(gift_info[1])
        number_of_receivers = int(gift_info[2])

        if money_to_gifts <= 0 or number_of_receivers <= 0:
            continue

        money_for_each = money_to_gifts // number_of_receivers
        total_spent = number_of_receivers * money_for_each

        members_balance[current_member_index] = current_member_balance - total_spent

        receivers_names = gift_info[3::]
        for receiver_name in receivers_names:
            receiver_index = members_names.index(receiver_name)
            receiver_balance = members_balance[receiver_index]
            members_balance[receiver_index] = receiver_balance + money_for_each

    for i in range(number_of_members):
        print(members_names[i], members_balance[i])
    if k < number_of_groups - 1:
        print()
