# 이진수 덧셈
# https://www.acmicpc.net/problem/1252

# https://robotai.tistory.com/37
# https://brownbears.tistory.com/467

import sys
input = sys.stdin.readline

binary1, binary2 = input().split()
print(format(int('0b' + binary1, 2) + int('0b' + binary2, 2), 'b'))
