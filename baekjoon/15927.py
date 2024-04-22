# 회문은 회문아니야!! ⚠️
# 24.04.22
# https://www.acmicpc.net/problem/15927
# 풀이 참고 : https://degurii.tistory.com/39

import sys
input=sys.stdin.readline

string = input().rstrip()
half_idx = len(string) // 2

if len(string) == 1:
    print(-1)
elif string[:half_idx] != string[-half_idx:][::-1]:
    print(string[:half_idx], string[-half_idx:])
    print(len(string))
elif string.count(string[0]) == len(string):
    print(-1)
else:
    print(len(string) - 1)
