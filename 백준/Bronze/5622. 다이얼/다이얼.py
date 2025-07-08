dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
word = input()
result = 0
for w in word:
    for idx, d in enumerate(dial):
        if w in d:
            result += idx + 3
print(result)