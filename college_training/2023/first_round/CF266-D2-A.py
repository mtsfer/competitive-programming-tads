seq_size = int(input())
stones_seq = input()
to_remove = 0
for i in range(0, seq_size - 1):
    if stones_seq[i] == stones_seq[i + 1]:
        to_remove += 1
print(to_remove)
