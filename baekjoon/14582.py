#오늘도 졌다
#https://www.acmicpc.net/problem/14582

team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))

sum1 = 0
sum2 = 0
win = 0
for i in range(9):
    sum1 += team1[i]
    if sum1 > sum2:
        win += 1
    sum2 += team2[i]

if win > 0 and sum1 < sum2:
    print("Yes")
else:
    print("No")
