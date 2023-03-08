# 생일
# 23.03.08
# 정렬
# https://www.acmicpc.net/problem/5635

N = int(input())
student = []
for _ in range(N):
    student.append(input().split())

student.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))
print(student[-1][0])
print(student[0][0])
