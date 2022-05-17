#주사위 게임
#https://www.acmicpc.net/problem/2476

N = int(input())

result = 0

for i in range(N):
    dice = list(map(int, input().split()))
    if dice.count(dice[0]) == 3:
        result = max(10000 + dice[0] * 1000, result)
    elif dice.count(dice[0]) == 2:
        result = max(1000 + dice[0] * 100, result)
    else:
        if dice.count(dice[1]) == 2:
            result = max(1000 + dice[1] * 100, result)
        else:
            result = max(max(dice) * 100, result)

print(result)
