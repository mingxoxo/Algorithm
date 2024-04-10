# 소수 ⚠️
# 24.04.10
# 풀이 참고: https://superohinsung.tistory.com/20
# https://www.acmicpc.net/problem/1312

A, B, N = map(int, input().split())

for i in range(N):
    A = (A % B) * 10
    result = A // B
    
print(result)
