number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
    number_of_bags, number_of_adjacents_bags_to_consider = map(int, input().split())
    bags_weight = list(map(int, input().split()))
    analyze_until = number_of_bags - number_of_adjacents_bags_to_consider + 1
    max_weight_sum_of_adjacents_bags = 0
    for i in range(0, analyze_until):
        weight_sum_of_adjacent_bags = 0
        for j in range(i, i + number_of_adjacents_bags_to_consider):
            weight_sum_of_adjacent_bags += int(bags_weight[j])
        if weight_sum_of_adjacent_bags > max_weight_sum_of_adjacents_bags:
            max_weight_sum_of_adjacents_bags = weight_sum_of_adjacent_bags
    print(f'A maior soma de pesos e {max_weight_sum_of_adjacents_bags}')
