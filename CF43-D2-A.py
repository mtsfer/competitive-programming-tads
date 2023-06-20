goals_to_win = (int(input()) // 2) + 1

teams = [input()]
goals_scored = [1, 0]

current_team_index = 0
while goals_scored[current_team_index] < goals_to_win:
    team = input()

    if team == teams[0]:
        current_team_index = 0
    else:
        current_team_index = 1
        if len(teams) == 1:
            teams.append(team)

    goals_scored[current_team_index] += 1

print(teams[current_team_index])
