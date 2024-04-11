number_of_cakes, time_to_bake, oven_capacity, time_to_build_a_oven = map(int, input().split())
if number_of_cakes <= oven_capacity:
    print("NO")
else:
    number_of_bakes_needed = (number_of_cakes // oven_capacity
                              if number_of_cakes % oven_capacity == 0
                              else number_of_cakes // oven_capacity + 1)
    time_to_bake_all_in_one_oven = time_to_bake * number_of_bakes_needed
    worth_build_oven_before_start = time_to_build_a_oven < time_to_bake
    there_is_two_ovens = worth_build_oven_before_start
    time_to_bake_all_in_two_ovens = time_to_build_a_oven if there_is_two_ovens else 0
    while number_of_cakes > 0:
        time_to_bake_all_in_two_ovens += time_to_bake
        if there_is_two_ovens:
            number_of_cakes -= 2 * oven_capacity
        else:
            number_of_cakes -= oven_capacity
            time_to_build_a_oven -= time_to_bake
            if time_to_build_a_oven < time_to_bake:
                time_to_bake_all_in_two_ovens += time_to_build_a_oven
                there_is_two_ovens = True
    print("YES" if time_to_bake_all_in_two_ovens < time_to_bake_all_in_one_oven else "NO")
