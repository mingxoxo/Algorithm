# 오등큰수 ⚠️
# 24.03.28
# 스택
# https://www.acmicpc.net/problem/17299
# 풀이참고: https://www.acmicpc.net/board/view/82926

from collections import Counter
import sys
input=sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
cnt_dict = Counter(arr)

ans = [-1] * N
stack = []

for i in range(N):
    while stack and cnt_dict[arr[stack[-1]]] < cnt_dict[arr[i]]:
        ans[stack.pop()] = arr[i]
    stack.append(i)

print(*ans)
