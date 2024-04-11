number_of_wires = int(input())
birds_per_wire = [int(x) for x in input().split()]
for shot in range(int(input())):
    wire, bird_position = map(int, input().split())
    wire_index = wire - 1
    if wire_index != 0:
        birds_per_wire[wire_index - 1] += bird_position - 1
    if wire_index != number_of_wires - 1:
        birds_per_wire[wire_index + 1] += birds_per_wire[wire_index] - bird_position
    birds_per_wire[wire_index] = 0
for birds in birds_per_wire:
    print(birds)
