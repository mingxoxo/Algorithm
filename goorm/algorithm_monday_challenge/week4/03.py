# 문제 3. 거리두기
# DP(동적 계획법)- Memoization, Bottom-up / 경우의 수
# 참고 : https://www.acmicpc.net/problem/1309

import sys
input = sys.stdin.readline

N = int(input())
d = 100000007

cnt = [1, 0, 0, 0, 0]
for _ in range(N):
	total = sum(cnt)
	cnt0 = total
	cnt1 = cnt[0] + cnt[2] + cnt[3]
	cnt2 = total - cnt[2]
	cnt3 = cnt[0] + cnt[1] + cnt[2]
	cnt4 = cnt[0] + cnt[2]
	cnt = [cnt0 % d, cnt1 % d, cnt2 % d, cnt3 % d, cnt4 % d]

print(sum(cnt)%d)