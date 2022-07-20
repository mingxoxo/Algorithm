# 타임 카드
# 22.07.20
# https://www.acmicpc.net/problem/5575

import sys
input = sys.stdin.readline

def cal_second(h, m, s):
    return s + m * 60 + h * 3600

for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    result = cal_second(h2, m2, s2) - cal_second(h1, m1, s1)
    print(result//3600, result%3600//60, result%3600%60);