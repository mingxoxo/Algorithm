# 카드 놓기
# 24.04.11
# https://www.acmicpc.net/problem/5568

from itertools import permutations

n = int(input())
k = int(input())
arr = [input() for _ in range(n)]

result = set()
for subarr in permutations(arr, k):
    result.add(''.join(subarr))
print(len(result))
