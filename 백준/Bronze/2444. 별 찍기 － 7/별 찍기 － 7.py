n = int(input())
for i in range(1, n):
    space = " " * (n - i)
    star = "*" * (2 * i - 1)
    print(space, star, sep="")
for i in range(n):
    space = " " * i
    star = "*" * (2 * (n - i) - 1)
    print(space, star, sep="")