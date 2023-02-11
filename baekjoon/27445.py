# Gorani Command
# 23.02.11

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
def check_cor(x, y, d):
    cor = set()
    for i in range(d + 1):
        cor.add((x + i, y + (d - i)))
        cor.add((x + i, y - (d - i)))
        cor.add((x - i, y + (d - i)))
        cor.add((x - i, y - (d - i)))
        
    return cor


result = set()
for i in range(N):
    dis = list(map(int, input().split()))
    for j in range(len(dis)):
        cor = check_cor(i + 1, j + 1, dis[j])
        result = result.intersection(cor) if result else cor
       
result = list(result)
print(result[0][0], result[0][1])
