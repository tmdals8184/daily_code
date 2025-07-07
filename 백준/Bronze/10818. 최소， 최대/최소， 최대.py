n = int(input())
num_arr = list(map(int, input().split()))
min, max = num_arr[0], num_arr[0]
for num in num_arr[1:]:
    if num > max:
        max = num
    if num < min:
        min = num
print(min, max)