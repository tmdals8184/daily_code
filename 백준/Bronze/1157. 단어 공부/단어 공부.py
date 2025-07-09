word = input()
abc_arr = [0] * 26
cap = word.upper() 
for w in cap:
    idx = ord(w) - ord("A") 
    abc_arr[idx] += 1
max_abc = max(abc_arr)
if abc_arr.count(max_abc) > 1:
    result = "?"
else:
    result = chr(ord("A") + abc_arr.index(max_abc))
print(result)