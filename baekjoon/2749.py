# 피보나치 수 3
# 23.03.07
# 피사노 주기
# https://www.acmicpc.net/problem/2749
# 공부 : https://comyoung.tistory.com/236

N = int(input())
fibonacci = [0, 1]
for i in range(2, min(15 * 100000 + 1, N + 1)):
    fibonacci.append((fibonacci[-2] + fibonacci[-1]) % 1000000)

print(fibonacci[N % 1500000])
