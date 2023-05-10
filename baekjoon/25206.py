# 너의 평점은
# 23.05.10
# https://www.acmicpc.net/problem/25206

score = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
         "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
total_credit = 0
result = 0

for _ in range(20):
    name, credit, grade = input().split()
    if grade == 'P':
        continue
    total_credit += float(credit)
    result += float(credit) * score[grade]

print("%.6f"%(result / total_credit))
