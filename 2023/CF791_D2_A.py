(limaksWeigh, bobWeigh) = map(lambda x: int(x), input().split())
currentYear = 0
while limaksWeigh <= bobWeigh:
    limaksWeigh *= 3
    bobWeigh *= 2
    currentYear += 1
print(currentYear)
