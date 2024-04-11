numberOfProblemsInTheContest: int = int(input())
problemsToBeSolved: int = 0
for i in range(0, numberOfProblemsInTheContest):
    if input().count('1') >= 2:
        problemsToBeSolved += 1
print(problemsToBeSolved)
