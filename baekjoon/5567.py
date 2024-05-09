# 결혼식
# 24.05.09
# https://www.acmicpc.net/problem/5567

from collections import defaultdict

import sys
input=sys.stdin.readline


n = int(input())
friends = defaultdict(set)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].add(b)
    friends[b].add(a)

invite_friends = set(friends[1])
for num in friends[1]:
    invite_friends.update(friends[num])

print(len(invite_friends - {1}))
