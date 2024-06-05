# 창문 닫기
# 24.06.05
# 수학, 정수론
# https://www.acmicpc.net/problem/13909

# 약수 개수가 홀수(연다)인가 짝수(닫는다)인가
N = int(input())
result = 0
i = 1

while i * i <= N:
    result += 1
    i += 1

print(result)
