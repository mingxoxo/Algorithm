# 너의 이름은 몇 점이니?
# https://www.acmicpc.net/problem/15813

N = int(input())
name = input()

print(sum([ord(c) - ord('A') + 1 for c in name]))
