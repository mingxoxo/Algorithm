# 로또
# 백트래킹
# 23.08.10
# https://www.acmicpc.net/problem/6603

def brute_force(nums, start, cnt, answer):
    if cnt == 0:
        print(*answer)
        return

    for i in range(start, len(nums)):
        answer.append(nums[i])
        brute_force(nums, i + 1, cnt - 1, answer)
        answer.pop()


while True:
    k, *nums = map(int, input().split())
    if k == 0:
        break
    brute_force(nums, 0, 6, [])
    print()
