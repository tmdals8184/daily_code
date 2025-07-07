"""
5 4
1 2 3
3 4 4
1 4 1
2 2 2
->
1 2 1 1 0
"""
n, m = map(int, input().split())
# 바구니 리스트
arr = [0 for _ in range(n)]
for _ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i - 1, j):
        arr[idx] = k
print(*arr, sep=" ")