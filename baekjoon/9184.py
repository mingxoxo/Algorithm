# 신나는 함수 실행
# 24.11.02
# DP
# https://www.acmicpc.net/problem/9184


dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
for a in range(0, 21):
    for b in range(0, 21):
        for c in range(0, 21):
            if a <= 0 or b <= 0 or c <= 0:
                dp[a][b][c] = 1
            elif a < b < c:
                dp[a][b][c] = dp[a][b][c - 1] + dp[a][b - 1][c - 1] - dp[a][b - 1][c]
            else:
                dp[a][b][c] = dp[a - 1][b][c] + dp[a - 1][b - 1][c] + dp[a - 1][b][c - 1] - dp[a - 1][b - 1][c - 1]
                


while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    
    if a <= 0 or b <= 0 or c <= 0:
        print(f'w({a}, {b}, {c}) = 1')
    elif a > 20 or b > 20 or c > 20:
        print(f'w({a}, {b}, {c}) = {dp[20][20][20]}')
    else:
        print(f'w({a}, {b}, {c}) = {dp[a][b][c]}')
    
    
