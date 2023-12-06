input()
available_officers_for_crimes_factor = 0
untreated_crimes = 0
for event in input().split():
    available_officers_for_crimes_factor += int(event)
    if available_officers_for_crimes_factor < 0:
        untreated_crimes += 1
        available_officers_for_crimes_factor = 0
print(untreated_crimes)
