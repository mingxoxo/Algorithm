# 좋은 친구
# 23.06.22
# https://www.acmicpc.net/problem/3078


import sys
input = sys.stdin.readline

import bisect
from collections import defaultdict

len_dict = defaultdict(list)

N, K = map(int, input().split())
for rank in range(N):
    name = input().rstrip()
    len_dict[len(name)].append(rank)

ans = 0
for len_list in len_dict.values():
    for i in range(len(len_list)):
        ans += bisect.bisect_right(len_list, len_list[i] + K) - (i + 1)

print(ans)


'''
풀이 2
# 슬라이딩 윈도우
# 공부: https://wooono.tistory.com/657

import sys
input = sys.stdin.readline


sliding_window = [0] * 21
students = []
ans = 0

N, K = map(int, input().split())
for end in range(N):
    students.append(len(input().rstrip()))
    if K < end:
        sliding_window[students[end - K - 1]] -= 1

    ans += sliding_window[students[end]]
    sliding_window[students[end]] += 1

print(ans)
'''
