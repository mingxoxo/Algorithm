# 과목선택
# https://www.acmicpc.net/problem/11948

science = sorted([int(input()) for _ in range(4)])
social_studies = sorted([int(input()) for _ in range(2)])
print(sum(science[1:]) + social_studies[1])
