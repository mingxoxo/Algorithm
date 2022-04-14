#벌집
#https://www.acmicpc.net/problem/2292

N = int(input())

cnt = 1
sum = 1
while(N > sum):
    sum += cnt*6
    cnt += 1

print(cnt)

