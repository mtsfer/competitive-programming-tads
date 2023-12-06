from math import pi

cup_diameter, initial_water_height, drinking_speed_in_ml_per_sec, growth_water_speed_in_cm_per_sec = map(int, input().split())

cup_radius = cup_diameter / 2

growth_water_speed_in_ml_per_sec = pi * cup_radius ** 2 * growth_water_speed_in_cm_per_sec

if growth_water_speed_in_ml_per_sec >= drinking_speed_in_ml_per_sec:
    print("NO")
else:
    speed_of_water_dicrease = drinking_speed_in_ml_per_sec - growth_water_speed_in_ml_per_sec
    initial_water_volume = pi * cup_radius ** 2 * initial_water_height

    print("YES")
    print(initial_water_volume / speed_of_water_dicrease)
