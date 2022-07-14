# 저항
# 22.07.15
# 구현 
# https://www.acmicpc.net/problem/1076

import sys
input = sys.stdin.readline


resistance = {"black":[0, 1], "brown":[1, 10], "red":[2, 100], "orange":[3, 1000],
              "yellow":[4, 10000], "green":[5, 100000], "blue":[6, 1000000],
              "violet":[7, 10000000], "grey":[8, 100000000], "white":[9, 1000000000]}

r1 = input().strip()
r2 = input().strip()
r3 = input().strip()

print((resistance[r1][0] * 10 + resistance[r2][0]) * resistance[r3][1])
