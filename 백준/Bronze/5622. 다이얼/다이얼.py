def get_num(val):
    num = ord(val) - ord("A")
    if num < 15:
        result = 2 + num // 3
    elif num < 19:
        result = 7
    elif num < 22:
        result = 8
    else:
        result = 9
    return result

word = input()
result = 0
for w in word:
    result += get_num(w) + 1
print(result)