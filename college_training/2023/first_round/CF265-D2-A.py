stones = input()
instructions = input()
liss_position = 0
for instruction in instructions:
    if instruction == stones[liss_position]:
        liss_position += 1
print(liss_position + 1)
