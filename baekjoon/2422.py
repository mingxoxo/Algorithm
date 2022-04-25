#한윤정이 이탈리아에 가서 아이스크림을 사먹는데
#https://www.acmicpc.net/problem/2422
#시간 초과 / 메모리 초과로 인해 다른 사람의 풀이를 참고함

from itertools import combinations

N, M = map(int, input().split())
no_combi = {i:[] for i in range(1, N+1)}

for i in range(M):
    c1, c2 = map(int, input().split())
    no_combi[c1].append(c2)
    no_combi[c2].append(c1)

combi = list(combinations([i+1 for i in range(N)], 3))
sum = 0

for c in combi:
    if c[0] in no_combi[c[1]] or c[0] in no_combi[c[2]] or c[1] in no_combi[c[2]]:
        continue
    sum += 1

print(sum)
