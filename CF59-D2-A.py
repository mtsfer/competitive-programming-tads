word = input()
caseFactor = 0
for letter in word:
    caseFactor += 1 if letter.islower() else -1
print(word.lower() if caseFactor >= 0 else word.upper())
