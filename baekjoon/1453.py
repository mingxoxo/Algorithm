# 피시방 알바
# https://www.acmicpc.net/problem/1453


import sys
input = sys.stdin.readline

N = int(input())
person = list(map(int, input().split()))
print(len(person) - len(set(person)))
