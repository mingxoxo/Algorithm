# Class Time
# 24.07.30
# 정렬
# https://www.acmicpc.net/problem/11609


students = sorted([input().split() for _ in range(int(input()))], key=lambda x: (x[1], x[0]))
for student in students:
    print(*student)
