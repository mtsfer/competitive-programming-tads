calories = input().split()
calories_spent = sum((int(calories[int(current_strip) - 1]) for current_strip in input()))
print(calories_spent)
