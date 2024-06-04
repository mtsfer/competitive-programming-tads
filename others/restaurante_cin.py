number_of_chefs, number_of_dishes = map(int, input().split())

times_to_finish_dishes = []
number_of_prepared_dishes = []

# Initialization
for _ in range(number_of_chefs):
    times_to_finish_dishes.append(0)
    number_of_prepared_dishes.append(0)

for _ in range(number_of_dishes):
    current_preparation_time = int(input())
    index_of_first_available_chef = 0
    min_preparation_time = times_to_finish_dishes[index_of_first_available_chef]
    if min_preparation_time != 0:
        for i in range(1, number_of_chefs):
            time_to_current_chef_become_available = times_to_finish_dishes[i]
            if time_to_current_chef_become_available >= min_preparation_time:
                continue
            index_of_first_available_chef = i
            min_preparation_time = time_to_current_chef_become_available
        for i in range(number_of_chefs):
            time_to_current_chef_become_available = times_to_finish_dishes[i]
            if time_to_current_chef_become_available == 0:
                continue
            times_to_finish_dishes[i] = time_to_current_chef_become_available - min_preparation_time
    number_of_prepared_dishes[index_of_first_available_chef] += 1
    times_to_finish_dishes[index_of_first_available_chef] = current_preparation_time

for i in range(number_of_chefs):
    print(i + 1, number_of_prepared_dishes[i], end='' if i == number_of_chefs - 1 else '\n')
