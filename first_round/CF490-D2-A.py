NUMBER_OF_SKILLS = TEAM_SIZE = 3

PROGRAMMING_SKILL = 1
MATHS_SKILL = 2
PHYSICAL_EDUCATION_SKILL = 3

number_of_children = int(input())
children_skills = input().split()
skill_groups = [[] for _ in range(NUMBER_OF_SKILLS)]
skill_groups_sizes = [0] * NUMBER_OF_SKILLS

for child in range(number_of_children):
    child_skill = int(children_skills[child])
    skill_groups[child_skill - 1].append(child + 1)
    skill_groups_sizes[child_skill - 1] += 1

teams = []
number_of_formed_teams = 0
is_possible_to_form_team = (skill_groups_sizes[PROGRAMMING_SKILL - 1] > 0 and
                            skill_groups_sizes[MATHS_SKILL - 1] > 0 and
                            skill_groups_sizes[PHYSICAL_EDUCATION_SKILL - 1] > 0)

while is_possible_to_form_team:
    teams.append([skill_groups[i][number_of_formed_teams] for i in range(TEAM_SIZE)])
    number_of_formed_teams += 1
    for i in range(NUMBER_OF_SKILLS):
        skill_groups_sizes[i] -= 1
        if skill_groups_sizes[i] == 0 and is_possible_to_form_team:
            is_possible_to_form_team = False

print(number_of_formed_teams)

if number_of_formed_teams > 0:
    for team in teams:
        team_formatted_output = ''
        for i in range(TEAM_SIZE):
            team_formatted_output += f'{team[i]} ' if i < TEAM_SIZE - 1 else str(team[i])
        print(team_formatted_output)
