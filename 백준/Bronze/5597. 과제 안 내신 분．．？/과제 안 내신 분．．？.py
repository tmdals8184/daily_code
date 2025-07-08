arr = [i + 1 for i in range(30)]
for i in range(28):
    submit = int(input())
    arr.remove(submit)
print(arr[0])
print(arr[1])