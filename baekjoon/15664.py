# N과 M (10)
# 백트래킹
# 24.12.01
# https://www.acmicpc.net/problem/15664

import sys
input=sys.stdin.readline

sys.setrecursionlimit(10**8)

ans_arr = set()

def recursive(cnt, start, ans):
    global N, nums
    
    if cnt == 0:
        if "".join(map(str, ans)) not in ans_arr:
            print(*ans)
            ans_arr.add("".join(map(str, ans)))
        return
    
    for i in range(start, N):
        ans.append(nums[i])
        recursive(cnt - 1, i + 1, ans)
        ans.pop()



N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
recursive(M, 0, [])
