number_of_cities = int(input())
cities_x_coordinates = list(map(int, input().split()))
for i in range(number_of_cities):
    current_city_coordinate = cities_x_coordinates[i]
    if i == 0:
        distance_to_nearest_city = abs(cities_x_coordinates[i + 1] - current_city_coordinate)
        distance_to_further_city = abs(cities_x_coordinates[number_of_cities - 1] - current_city_coordinate)
    elif i == number_of_cities - 1:
        distance_to_nearest_city = abs(current_city_coordinate - cities_x_coordinates[i - 1])
        distance_to_further_city = abs(current_city_coordinate - cities_x_coordinates[0])
    else:
        distance_to_next_left_city = abs(current_city_coordinate - cities_x_coordinates[i - 1])
        distance_to_next_right_city = abs(cities_x_coordinates[i + 1] - current_city_coordinate)
        distance_to_nearest_city = (distance_to_next_left_city
                                    if distance_to_next_left_city < distance_to_next_right_city
                                    else distance_to_next_right_city)
        distance_to_leftmost_city = abs(current_city_coordinate - cities_x_coordinates[0])
        distance_to_rightmost_city = abs(cities_x_coordinates[number_of_cities - 1] - current_city_coordinate)
        distance_to_further_city = (distance_to_leftmost_city
                                    if distance_to_leftmost_city > distance_to_rightmost_city
                                    else distance_to_rightmost_city)
    print(distance_to_nearest_city, distance_to_further_city)
