# 조합
# 수학 / 조합론 / 큰 수 연산
# 22.10.27
# https://www.acmicpc.net/problem/2407
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=dudwo567890&logNo=130165177493

import sys
from fractions import Fraction
input = sys.stdin.readline


n, m = map(int, input().split())
result = 1

for i in range(m):
    result *= Fraction(n - i)
    result = Fraction(result, m - i)

print(result)
