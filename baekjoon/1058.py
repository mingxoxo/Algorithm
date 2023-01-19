# 친구
# 플로이드 워셜
# 22.01.19
# https://www.acmicpc.net/problem/1058

import sys
import copy
input = sys.stdin.readline

N = int(input())
friend = []

for i in range(N):
    arr = list(input().strip())
    friend.append([j for j in range(N) if arr[j] == 'Y'])

result = 0

for i in range(N):
    cnt_set = set(friend[i].copy())
    for j in friend[i]:
        cnt_set = cnt_set.union(set(friend[j]))
    try:
        cnt_set.remove(i)
    except:
        pass
    result = max(result, len(cnt_set))
            
print(result)
