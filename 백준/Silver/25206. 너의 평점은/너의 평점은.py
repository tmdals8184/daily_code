score_dict = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0,
    "P" : -1.0
}
t_credit = 0
t_score = 0
for _ in range(20):
    _, credit, grade = input().split()
    credit = float(credit)
    score = score_dict[grade]
    if score < 0:
        continue
    t_credit += credit
    t_score += credit * score
print("{:.6f}".format(t_score / t_credit))