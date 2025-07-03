A, B, C = map(int, input().split())
# 첫째 줄에 , 둘째 줄에 , 셋째 줄에 , 넷째 줄에 를 출력한다.
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)