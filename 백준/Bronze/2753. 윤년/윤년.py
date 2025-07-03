y = int(input())

def is_mul(num1, num2):
    return num1 % num2 == 0

if (is_mul(y, 4) and not is_mul(y, 100)) or is_mul(y, 400):
    print("1")
else:
    print("0")