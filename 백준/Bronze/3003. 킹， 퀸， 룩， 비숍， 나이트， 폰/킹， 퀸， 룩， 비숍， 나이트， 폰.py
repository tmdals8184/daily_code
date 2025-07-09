chess_arr = [1, 1, 2, 2, 2, 8]
l = len(chess_arr)
in_arr = list(map(int, input().split()))
out_arr = [c - i for c, i in zip(chess_arr, in_arr)]
print(*out_arr, sep=" ")