# 귀여운 라이언
# 22.08.08
# 투포인터
# https://www.acmicpc.net/problem/15565

N, K = map(int, input().split())
doll = list(map(int, input().split()))

start = 0
end = 0
cnt = 0
arr = []
result = -1

while end < N:
    if doll[end] == 1:
        cnt += 1
        arr.append(end)
    if cnt == K:
        result = min(result, end - arr[start] + 1) if result != -1 else end - arr[start] + 1
        start += 1
        cnt -= 1
    end += 1

print(result)
