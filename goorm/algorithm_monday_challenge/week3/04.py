# 문제 4. 순환하는 수로
# DFS / 사이클 판단
# 어려움 별 5개,, - BFS 작성 코드는 틀림
# sys.setrecursionlimit(10**8)를 해주지 않으면 runtimeerror

# 문제 해설 - DFS
# i번에서 출발한 물이 이동 조건에 따라 흐른다. 이때 방문한 적이 있는 물탱크에 도착한다면,
# 이는 현재 순환하는 수로라고 할 수 있다.
# i번에서 출발한 물이 이동 조건에 따라 흐른다. 이때 방문한 적 있는 물탱크에 도착했고,
# 물탱크의 번호가 i번이라면 순환하는 수로의 시작과 끝을 찾았다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
from collections import deque, defaultdict


N = int(input())
channel = defaultdict(list)
for _ in range(N):
	a, b = map(int, input().split())
	channel[a].append(b)
	channel[b].append(a)


'''
vistied = 방문 여부 모두 기록
finded = 방금 전 방문 여부
tar = 공급 물탱크
'''

visited = [0 for _ in range(N+1)]
circle = list()
finded = -1


# 탐색 재귀
def FindCycle(u, tar):
	global finded

	if visited[u] == 1:  # 이미 방문 -> 순환 구조 (순환 고리는 단 1개)
		finded = u
		if u not in circle:
			circle.append(u)
		return

	visited[u] = 1
	for i in channel[u]:

		if i == tar:  # 공급 물탱크면 넘어가기
			continue

		FindCycle(i, u)  # 방문 X, 공급한 물탱크가 아니라면 새로운 탐색지점

		if finded == -2:  # 이미 발견된 순환고리 값이라면 탐색 정지
			return
		if finded == u:  # finded == u라면 이미 방문 지점이라 탐색 정지
			finded = -2
			return

		if finded >= 0: # 새롭게 발견된 순환 고리
			if u not in circle:
				circle.append(u)
			return

FindCycle(1, 1)

# 저장된 순한 값 정렬
circle.sort()

# 순환의 길이
print(len(circle))

# 순환 오름차순으로 출력
for i in circle:
	print(i, end = ' ')



#
# def DFS(channel, N):
# 	visited = [0 for _ in range(N)]
# 	queue = deque([0])
# 	while queue:
# 		tank = queue.pop() # popleft(BFS) -> pop(DFS)
#
# 		for i in channel[tank]:
# 			if visited[i] == 0:
# 				visited[i] = 1
# 				queue.append(i)

#
# def BFS(channel, N):
# 	queue = deque([[1, [1]]])
# 	rcnt = 0
# 	rtank = []
# 	while queue:
# 		cnt, tank = queue.popleft()
#
# 		if 3 <= cnt - 1 and tank[0] == tank[-1]:
# 			if rcnt < cnt - 1:
# 				rcnt, rtank = cnt - 1, tank[1:]
# 			continue
#
# 		for i in channel[tank[-1]]:
# 			if 2 <= cnt and tank[-2] == i:
# 				continue
# 			queue.append([cnt + 1, tank + [i]])
#
# 	return rcnt, rtank