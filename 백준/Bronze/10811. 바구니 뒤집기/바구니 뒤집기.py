# 1, 2, 3, 4, 5
# 2, 1, 3, 4, 5
# 2, 1, 4, 3, 5
# 3, 4, 1, 2, 5

n, m = map(int, input().split())
arr = [i + 1 for i in range(n)]
for idx in range(m):
    i, j = map(int, input().split())
    arr[i - 1 : j] = arr[i - 1 : j][::-1]
print(*arr, sep=" ")