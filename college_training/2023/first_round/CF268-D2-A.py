quantity_of_teams = int(input())
teams_uniforms = list(input().split() for i in range(quantity_of_teams))
quantity_of_host_as_guest = 0
for i in range(quantity_of_teams):
    for j in range(quantity_of_teams):
        if i != j and teams_uniforms[i][0] == teams_uniforms[j][1]:
            quantity_of_host_as_guest += 1
print(quantity_of_host_as_guest)
