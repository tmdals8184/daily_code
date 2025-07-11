word = input()
cro_map = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for cro in cro_map:
    word = word.replace(cro, "*")
print(len(word))