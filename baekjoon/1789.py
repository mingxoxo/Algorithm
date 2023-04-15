# 수들의 합
# 그리디
# https://www.acmicpc.net/problem/1789

# 명확한 설명: https://konghana01.tistory.com/53

S = int(input())
ssum = 0
idx = 0

while S >= ssum:
    idx += 1
    ssum += idx
    

print(idx - 1)
