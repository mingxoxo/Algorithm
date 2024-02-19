# 문자열 게임 2
# 24.02.19
# 문자열, 슬라이딩 윈도우
# https://www.acmicpc.net/problem/20437

import sys
input=sys.stdin.readline

T = int(input())
for _ in range(T):
    W = input().rstrip()
    K = int(input())
    count_dict = {chr(ch): [] for ch in range(ord('a'), ord('z') + 1)}
    
    for i, ch in enumerate(W):
        count_dict[ch].append(i)
        
    min_len = len(W) + 1
    max_len = 0
    for ch in range(ord('a'), ord('z') + 1):
        arr = count_dict[chr(ch)]
        for i in range(K - 1, len(arr)):
            min_len = min(min_len, arr[i] - arr[i - K + 1] + 1)
            max_len = max(max_len, arr[i] - arr[i - K + 1] + 1)
    
    if (min_len == len(W) + 1 and max_len == 0):
        print(-1)
    else:
        print(min_len, max_len)
