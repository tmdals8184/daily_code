arr = [int(input()) for _ in range(9)]
max_val = max(arr)
max_idx = arr.index(max_val) + 1
print(max_val)
print(max_idx)