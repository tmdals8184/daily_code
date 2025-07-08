# 1, 2, 3, 4, 5
# 2, 1, 3, 4, 5
# 2, 1, 4, 3, 5
# 3, 1, 4, 2, 5
# 3, 1, 4, 2, 5

n, m = map(int, input().split())
arr = [i + 1 for i in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    arr[i - 1], arr[j - 1] = arr[j - 1], arr[i - 1]
print(*arr, sep=" ")