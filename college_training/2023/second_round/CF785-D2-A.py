number_of_polyhedrons = int(input())

total_of_faces = 0

for _ in range(number_of_polyhedrons):
    polyhedron_name_first_letter = input()[0]

    if polyhedron_name_first_letter == 'T':
        total_of_faces += 4
    elif polyhedron_name_first_letter == 'C':
        total_of_faces += 6
    elif polyhedron_name_first_letter == 'O':
        total_of_faces += 8
    elif polyhedron_name_first_letter == 'D':
        total_of_faces += 12
    else:
        total_of_faces += 20

print(total_of_faces)
