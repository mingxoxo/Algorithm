# 기상캐스터
# 구현, 시뮬레이션
# 24.03.06
# https://www.acmicpc.net/problem/10709


H, W = map(int, input().split())
for _ in range(H):
    ans = -1
    for ch in input():
        if ch == 'c':
            ans = 0
        print(ans, end=' ')
        if ans != -1:
            ans += 1
    print()
    
