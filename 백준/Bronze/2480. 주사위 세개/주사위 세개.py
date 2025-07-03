a, b, c = map(int, input().split())
if a == b:
    if b == c:
        print(a * 1000 + 10000)
    else:
        print(a * 100 + 1000)
else:
    if a == c:
        print(a * 100 + 1000)
    elif b == c:
        print(b * 100 + 1000)
    else:
        r = a if a > b else b
        r = r if r > c else c
        print(r * 100)