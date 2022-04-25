#ATM
#그리디 알고리즘
#https://www.acmicpc.net/problem/11399

N = int(input())
time_list = list(map(int, input().split()))
time_list.sort()

sum = 0
for i in range(N):
    sum += (N-i)*time_list[i]

print(sum)

