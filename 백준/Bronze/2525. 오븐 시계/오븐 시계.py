h, m = map(int, input().split())
t = int(input())
t_h, t_m = t // 60, t % 60

if m + t_m < 60:
    r_m = m + t_m
    if h + t_h < 24:
        r_h = h + t_h
    else:
        r_h = h + t_h - 24
else:
    r_m = m + t_m - 60
    if h + t_h + 1 < 24:
        r_h = h + t_h + 1
    else:
        r_h = h + t_h + 1 - 24
print(r_h, r_m)