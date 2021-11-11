#https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

def solution(n, computers):
    #BFS
    visited = [0 for i in range(n)] #방문 체크
    answer = 0

    while sum(visited) != n:
        firstSearch = visited.index(0)
        queue = deque([firstSearch])
        while queue:
            node = queue.popleft()
            if visited[node] == 1: # 방문한 적이 있다면 돌아간다.
                continue
            visited[node] = 1 #방문했다고 표시
            for i in range(n):
                if computers[node][i] == 1 and visited[i] == 0:
                    queue.append(i)
        answer+=1
    return answer
  
  #비슷한 방식으로 DFS로 풀거나 플루이드 워셜 알고리즘을 사용하신 분이 있었음
  #함수 안에 BFS부분을 함수로 두어 깔끔하게 풀 수도 있음
