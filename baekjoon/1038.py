# 감소하는 수
# 브루트포스, 백트래킹
# 24.01.08
# https://www.acmicpc.net/problem/1038

def brute_force(N=0):
    for i in range(10):
        num = N * 10 + i
        if 0 < num < 10 or num % 10 < num % 100 // 10:
            arr.append(num)
            brute_force(num)


N = int(input())
if 1023 <= N:
    print(-1)
else:
    arr = [0]
    brute_force()
    arr.sort()
    print(arr[N])
