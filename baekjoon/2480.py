#주사위 세개
#https://www.acmicpc.net/problem/2480

dice = list(map(int, input().split()))

if dice.count(dice[0]) == 3:
    print(10000+dice[0]*1000)
elif dice.count(dice[0]) == 2:
    print(1000 + dice[0] * 100)
elif dice.count(dice[1]) == 2:
    print(1000 + dice[1] * 100)
else:
    print(max(dice)*100)

