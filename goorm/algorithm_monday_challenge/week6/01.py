# 문제 1. 7게임
# 문자열 / 사칙연산

for i in range(5):
    num = list(map(int, input()))
    a = 0
    b = 1
    for j in range(7):
        if j % 2 == 0:
            a += num[j]
        elif num[j] != 0:
            b *= num[j]
    print((a * b) % 10)