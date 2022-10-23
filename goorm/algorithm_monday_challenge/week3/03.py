# 문제 3. 구름이의 여행
# BFS/DFS / 그래프 구현

import sys
from collections import deque

input = sys.stdin.readline


def BFS(bridge, N, M):
	visited = [False] * (N + 1)
	visited[1] = True

	queue = deque([(1, 0)])
	while queue:
		island, cnt = queue.popleft()
		if island == N:
			return cnt

		for i in bridge[island]:
			if visited[i] == False:
				visited[i] = True
				queue.append((i, cnt + 1))

	return M + 1


N, M, K = map(int, input().split())
bridge = {i: [] for i in range(1, N + 1)}
for _ in range(M):
	u, v = map(int, input().split())
	bridge[u].append(v)
	bridge[v].append(u)

print("YES") if BFS(bridge, N, M) <= K else print("NO")


# 문제 해설

# 아래의 코드를 defaultdict 라이브러리로 해결
# graph = defaultdict(list)
# bridge = {i: [] for i in range(1, N + 1)} -> 메모리 낭비

# visited 함수로 다리 이용 횟수를 저장
# 이 문제는 첫 방문이 바로 최단거리가 됨