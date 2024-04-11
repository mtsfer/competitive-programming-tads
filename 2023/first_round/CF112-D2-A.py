s1 = input().lower()
s2 = input().lower()
comparisonResult = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        comparisonResult = 1 if s1[i] > s2[i] else -1
        break
print(comparisonResult)
