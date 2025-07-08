words = input().split()
rev_nums = [int(w[::-1]) for w in words]
print(max(rev_nums))