# 리모컨
# Brute Force
# 23.08.24
# https://www.acmicpc.net/problem/1107


N = int(input())
channel = 100
M = int(input())
broken = set(input().split()) if M != 0 else set()
butten = set(list('0123456789')) - broken

answer = N - channel if channel <= N else channel - N
low_channel = high_channel = N
while 0 <= low_channel:
    if len(set(str(low_channel)) - butten) == 0:
        answer = min(answer, N - low_channel + len(str(low_channel)))
        break
    low_channel -= 1

if len(butten - set('0')) != 0:
    while True:
        if len(set(str(high_channel)) - butten) == 0:
            answer = min(answer, high_channel - N + len(str(high_channel)))
            break
        high_channel += 1
    
print(answer)
