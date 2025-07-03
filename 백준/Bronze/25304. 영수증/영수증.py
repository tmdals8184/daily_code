total = int(input())
typ = int(input())
s = 0
for i in range(typ):
    price, n = map(int, input().split())
    s += price * n
print("Yes" if total == s else "No")