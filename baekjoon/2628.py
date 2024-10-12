# 종이자르기
# 구현, 정렬
# 24.10.12
# https://www.acmicpc.net/problem/2628


def get_max_gap(arr):
    arr.sort()
    return max([arr[i + 1] - arr[i] for i in range(len(arr) - 1)])


row, col = map(int, input().split())

rows = [0, row]
cols = [0, col]

for _ in range(int(input())):
    cmd, num = map(int, input().split())
    
    if cmd == 0:
        cols.append(num)
    elif cmd == 1:
        rows.append(num)

print(get_max_gap(rows) * get_max_gap(cols))
