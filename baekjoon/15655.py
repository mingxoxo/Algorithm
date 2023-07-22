# N과 M (6)
# 백트래킹
# 23.07.22
# https://www.acmicpc.net/problem/15655

def backtracking(ans, start_idx):
    global N, M
    
    if len(ans) == M: 
        print(*ans)
    
    for i in range(start_idx, N):
        ans.append(nums[i])
        backtracking(ans, i + 1)
        ans.pop()


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
backtracking([], 0)
