# 양팔저울
# 그리디
# 23.10.26
# https://www.acmicpc.net/problem/25943

N = int(input())
stone = list(map(int, input().split()))
left, right = stone[0], stone[1]
for i in range(2, N):
    if left > right:
        right += stone[i]
    else:
        left += stone[i]

diff = abs(left - right)
weight = [100, 50, 20, 10, 5, 2, 1]
result = 0
for w in weight:
    if diff < w:
        continue
    result += diff // w
    diff %= w

print(result)
