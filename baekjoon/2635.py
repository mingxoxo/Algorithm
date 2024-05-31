# 수 이어가기
# 24.05.31
# 브루트포스
# https://www.acmicpc.net/problem/2635

def check_rule(a, b):
    cnt = 2
    arr = [a, b]

    while arr[-2] >= arr[-1]:
        arr.append(arr[-2] - arr[-1])
        cnt += 1

    return cnt, arr

N = int(input())

result_cnt = 0
result_arr = []
b = N // 2

while True:
    cnt, arr = check_rule(N, b)
    if result_cnt < cnt:
        result_cnt = cnt
        result_arr = arr

    if cnt == 2:
        break
    b += 1

print(result_cnt)
print(*result_arr)
