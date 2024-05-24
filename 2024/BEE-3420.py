from math import sqrt

n = int(input())
for _ in range(n):
    c = int(input())
    x = (sqrt(24 * c + 1) - 1) / 6
    print(int(x))

