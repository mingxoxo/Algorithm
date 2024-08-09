# 빈도 정렬
# 24.08.09
# 정렬
# https://www.acmicpc.net/problem/2910


from collections import Counter

N, C = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = Counter(numbers)
sorted_numbers = sorted(numbers, key=lambda x: (-cnt[x], numbers.index(x)))
print(*sorted_numbers)
