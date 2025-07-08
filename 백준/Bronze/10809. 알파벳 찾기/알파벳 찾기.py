word = input()
# letters = [chr(ord("a") + i) for i in range(26)]
# for i, v in enumerate(letters):
#     letters[i] = word.find(v)
# print(*letters, sep=" ")
letters = []
for i in range(26):
    val = chr(ord("a") + i)
    letters.append(word.find(val))
print(*letters, sep=" ")