# 스타트와 링크
# 브루트포스
# 23.07.02
# https://www.acmicpc.net/problem/14889

from itertools import combinations

def getTeamPower(players):
    global power

    result = 0
    for p1 in players:
        for p2 in players:
            result += power[p1][p2]

    return result


N = int(input())
power = [list(map(int, input().split())) for _ in range(N)]
ans = 10**9
all_players = set([i for i in range(N)])

for team1 in combinations(all_players, N//2):
    team2 = all_players - set(team1)
    ans = min(ans, abs(getTeamPower(team1) - getTeamPower(team2)))

print(ans)
