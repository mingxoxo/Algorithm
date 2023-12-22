# Contact
# 23.12.22
# 정규표현식
# https://www.acmicpc.net/problem/1013
# 참고: https://engineer-mole.tistory.com/189

import re
import sys
input=sys.stdin.readline

T = int(input())
for _ in range(T):
    result = re.fullmatch(r'(100+1+|01)+', input().rstrip())
    print('NO') if result is None else print('YES')
