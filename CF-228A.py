valera_shoes = input().split()
equal_shoes = []
for i in range(0, 4):
    under_analysis_shoe = valera_shoes[i]
    for j in range(0, i):
        previous_shoe = valera_shoes[j]
        if under_analysis_shoe == previous_shoe:
            equal_shoes.append(previous_shoe)
            break
print(len(equal_shoes))
