# 준석이의 수학 숙제
# 23.09.14
# https://www.acmicpc.net/problem/17206

import itertools
import bisect
import sys
input=sys.stdin.readline


T = int(input())
nums = list(map(int, input().split()))
multiples = [i for i in range(3, max(nums) + 1) if i % 3 == 0 or i % 7 == 0]
accumulate_result = list(itertools.accumulate(multiples))

for n in nums:
    print(accumulate_result[bisect.bisect_right(multiples, n) - 1])
