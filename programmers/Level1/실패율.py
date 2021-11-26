#https://programmers.co.kr/learn/courses/30/lessons/42889
#실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수/스테이지에 도달한 플레이어 수
#N : 전체 스테이지 개수
#stages : 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열

#실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담겨있는 배열을 리턴

import heapq

def solution(N, stages):
    fail = {}
    heapq.heapify(stages)
    for i in range(1, N+1):
        fail[i] = len(stages)
        cnt = 0
        while stages and stages[0] == i:
            cnt+=1
            heapq.heappop(stages)
        if not stages:
            continue
        fail[i] = cnt / fail[i]
    answer = list(dict(sorted(fail.items(), reverse=True, key = lambda x:x[1])).keys())
    #answer = sorted(fail , reverse=True, key = lambda x:fail[x]) 로 줄일 수 있다.
    return answer
