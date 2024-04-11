MIN_NEEDED_FSHIPS_PER_CITIZEN = 2

number_of_citizens, number_of_fships_preserved_on_notebook = map(int, input().split())

citizens_identifiers = input().split()
citizens_fships = {}

for identifier in citizens_identifiers:
    citizens_fships[identifier] = []

for _ in range(number_of_fships_preserved_on_notebook):
    friend1, friend2 = input().split()
    citizens_fships[friend1].append(friend2)
    citizens_fships[friend2].append(friend1)

total_of_lacking_friends = 0
for citizen, fships in citizens_fships.items():
    fships_number = len(fships)
    if fships_number < MIN_NEEDED_FSHIPS_PER_CITIZEN:
        total_of_lacking_friends += MIN_NEEDED_FSHIPS_PER_CITIZEN - fships_number

if total_of_lacking_friends == 0:
    print("Nenhum registro perdido")
    exit(0)

needed_friendships = total_of_lacking_friends // 2 + (total_of_lacking_friends % 2)

print(f'Precisamos de {needed_friendships} amigacoes')
